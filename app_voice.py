from flask import Flask, request, jsonify, render_template
import time
import logging
from config import Config
from services.speech_service import SpeechService
from services.llm_service import LLMService
from services.file_service import FileService
from services.text_parser import parse_refined_text_voice

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    """Render the application frontend."""
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    """Handle file uploads and processing."""
    # Check if a file is uploaded
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400
    
    audio_file = request.files["audio"]
    input_text = request.form.get('text', '')
    
    # Validate file
    if audio_file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
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

        # Step 2: Process the HTML input text
        HTML_start_time = time.time()
        json_data = LLMService.process_html_data(
            input_text,
            app.config["FIREWORKS_API_KEY"]
        )
        HTML_time = time.time() - HTML_start_time
        logging.info(f"Time taken to process HTML with LLM: {HTML_time:.4f} seconds")

        # Step 3: Process the transcription with LLM
        text_start_time = time.time()
        refined_text = LLMService.process_voice_data(
            raw_text, 
            json_data,
            app.config["FIREWORKS_API_KEY"]
        )
        extract_time = time.time() - text_start_time
        logging.info(f"Time taken to process text with LLM: {extract_time:.4f} seconds")

        # Step 4: Parse the refined text
        parsed_text, json_data, reasoning = parse_refined_text_voice(refined_text)
        
        # Track processing time
        processing_time = time.time() - process_start_time
        logging.info(f"the Total Processing time: {processing_time:.4f} seconds")

        # Clean up the temporary file
        FileService.cleanup_file(file_path)
        
        # Return the results
        return jsonify({
            "raw_text": raw_text,
            "refined_text": parsed_text,
            "json_data": json_data,
            "reasoning": reasoning,
        })
    
    except Exception as e:
        # Clean up the temporary file in case of error
        FileService.cleanup_file(file_path)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8586)
