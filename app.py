from flask import Flask, request, jsonify, render_template
from models import llm, speech_reco
import os
import uuid  # Import uuid for generating unique filenames
from utlis import parse_refined_text
import time

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Function to generate a unique filename
def generate_unique_filename(filename):
    # Generate a unique filename using UUID
    unique_id = uuid.uuid4().hex
    _, ext = os.path.splitext(filename)  # Split filename and extension
    return f"{unique_id}{ext}"  # Combine unique ID and original extension


# Function to clean up the uploads directory
def cleanup_uploads(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File removed: {file_path}")
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error removing file: {str(e)}")


@app.route("/")
def index():
    # Render the HTML frontend
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    # Check if a file is uploaded
    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio_file = request.files["audio"]
    input_text = request.form['text']
    # Validate file type and size
    if audio_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Generate a unique filename to avoid conflicts
    unique_filename = generate_unique_filename(audio_file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)

    # Save the uploaded file
    try:
        audio_file.save(file_path)
        print(f"File saved to: {file_path}")  # Debugging
    except Exception as e:
        return jsonify({"error": f"Failed to save file: {str(e)}"}), 500

    # Transcribe the audio
    try:
        start_SR = time.time()
        raw_text = speech_reco(file_path)
        end_SR = time.time()
        print("Time cost of whisper: ", end_SR - start_SR)
    except Exception as e:
        return jsonify({"error": f"Speech recognition failed: {str(e)}"}), 500

    # Parse the refined text into structured data
    try:
        json_data = llm(task="text", raw_text=input_text)
        refined_text = llm(task="voice", raw_text=raw_text, html_text=json_data)
        parsed_text, json_data, reasoning = parse_refined_text(refined_text)
        print("json data: ", json_data)
    except Exception as e:
        return jsonify({"error": f"Text parsing failed: {str(e)}"}), 500

    # Clean up the uploads directory
    cleanup_uploads(file_path)
    
    # Return the results
    return jsonify({
        "raw_text": raw_text,
        "refined_text": parsed_text,
        "json_data": json_data,
        "reasoning": reasoning
    })

if __name__ == "__main__":
    app.run(debug=True, port=8586)