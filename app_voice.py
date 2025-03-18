from flask import Flask, request, jsonify, render_template
import time
import logging
import os
import json
from config import Config
from src.speech_service import SpeechService
from src.llm_service import LLMService
from src.file_service import FileService
from src.text_parser import parse_refined_text_voice
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Database setup
Base = declarative_base()

class ProcessedAudio(Base):
    __tablename__ = 'processed_audio'
    
    id = Column(Integer, primary_key=True)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(512), nullable=False)
    raw_text = Column(Text)
    refined_text = Column(Text)
    json_data = Column(JSON)
    reasoning = Column(Text)
    form_name = Column(String(255))
    voice_processing_time = Column(Float)
    llm_processing_time = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'file_path': self.file_path,
            'raw_text': self.raw_text,
            'refined_text': self.refined_text,
            'json_data': self.json_data,
            'reasoning': self.reasoning,
            'form_name': self.form_name,
            'voice_processing_time': self.voice_processing_time,
            'llm_processing_time': self.llm_processing_time,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# Create database engine and session
def setup_database():
    db_url = app.config["DATABASE_URL"]
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def load_forms_dataframe():
    # Example implementation - replace with your actual dataframe loading code
    # This could be from a CSV, database, or any other source
    try:
        return pd.read_parquet("data_latest.parquet", engine="pyarrow")  # Adjust path as needed
    except Exception as e:
        logging.error(f"Error loading forms dataframe: {str(e)}")
        # Return an empty dataframe with the expected columns if loading fails
        return pd.DataFrame(columns=['name', 'json_format'])

@app.route("/")
def index():
    """Render the application frontend."""
    return render_template("index.html")

@app.route("/get_forms")
def get_forms():
    """Return the list of available forms."""
    try:
        forms_df = load_forms_dataframe()
        # Convert dataframe to list of dictionaries for JSON response
        forms_list = forms_df[['name', 'json_format']].to_dict(orient='records')
        return jsonify(forms_list)
    except Exception as e:
        logging.error(f"Error retrieving forms: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/upload", methods=["POST"])
def upload():
    """Handle file uploads and processing."""
    # Check if a file is uploaded
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400
    
    audio_file = request.files["audio"]
    form_name = request.form.get('formName', '')
    form_json_format = request.form.get('formJsonFormat', '')
    
    # Validate file
    if audio_file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    # Initialize database session
    db_session = setup_database()
    
    # Save the uploaded file
    try:
        file_path = FileService.save_file(audio_file, app.config["UPLOAD_FOLDER"])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    try:
        # Process the uploaded file
        process_start_time = time.time()
        
        # Step 1: Transcribe the audio
        raw_text = SpeechService.transcribe_audio(
            file_path,
            app.config["GROQ_API_KEY"]
        )
        voice_time = time.time() - process_start_time
        logging.info(f"Time taken to process voice with WHISPER: {voice_time:.4f} seconds")
        
        # Step 2: Process the transcription with LLM
        text_start_time = time.time()
        refined_text = LLMService.process_voice_data(
            raw_text,
            form_json_format,
            app.config["FIREWORKS_API_KEY"]
        )
        extract_time = time.time() - text_start_time
        logging.info(f"Time taken to process text with LLM: {extract_time:.4f} seconds")
        
        # Step 3: Parse the refined text
        parsed_text, json_data, reasoning = parse_refined_text_voice(refined_text)
        
        # Track processing time
        processing_time = time.time() - process_start_time
        logging.info(f"Total Processing time: {processing_time:.4f} seconds")
        
        # Save results to database
        processed_record = ProcessedAudio(
            filename=audio_file.filename,
            file_path=file_path,
            raw_text=raw_text,
            refined_text=parsed_text,
            json_data=json_data,
            reasoning=reasoning,
            form_name=form_name,
            voice_processing_time=voice_time,
            llm_processing_time=extract_time
        )
        
        db_session.add(processed_record)
        db_session.commit()
        
        # Return the results
        return jsonify({
            "id": processed_record.id,
            "raw_text": raw_text,
            "refined_text": parsed_text,
            "json_data": json_data,
            "reasoning": reasoning,
        })
    except Exception as e:
        # Rollback the session in case of error
        db_session.rollback()
        # Clean up the temporary file in case of error
        FileService.cleanup_file(file_path)
        return jsonify({"error": str(e)}), 500
    finally:
        # Close the database session
        db_session.close()

@app.route("/processed_records", methods=["GET"])
def get_processed_records():
    """Retrieve all processed records."""
    try:
        db_session = setup_database()
        records = db_session.query(ProcessedAudio).all()
        result = [record.to_dict() for record in records]
        db_session.close()
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error retrieving processed records: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/processed_record/<int:record_id>", methods=["GET"])
def get_processed_record(record_id):
    """Retrieve a specific processed record by ID."""
    try:
        db_session = setup_database()
        record = db_session.query(ProcessedAudio).filter_by(id=record_id).first()
        
        if record is None:
            db_session.close()
            return jsonify({"error": "Record not found"}), 404
        
        result = record.to_dict()
        db_session.close()
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error retrieving processed record: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure the database tables exist
    setup_database()
    app.run(debug=True, port=8586)