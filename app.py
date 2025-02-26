from flask import Flask, request, jsonify, render_template
from src.LLM import llm, speech_reco
import os
from src.utlis import parse_refined_text
import time

app = Flask(__name__)

# Define the upload folder
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    # Render the HTML frontend
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_audio():
    # Check if a file is uploaded
    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio_file = request.files["audio"]

    # Validate file type and size
    if audio_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file
    try:
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_file.filename)
        audio_file.save(file_path)
    except Exception as e:
        return jsonify({"error": f"Failed to save file: {str(e)}"}), 500

    # Transcribe the audio
    try:
        start_SR = time.time()
        raw_text = speech_reco(file_path)
        end_SR = time.time()
        print("Time cost of whisper: ", end_SR - start_SR)
        # print(f"Raw text: {raw_text}")  # Debugging
    except Exception as e:
        return jsonify({"error": f"Speech recognition failed: {str(e)}"}), 500

    # Parse the refined text into structured data
    try:
        start_llm = time.time()
        refined_text = llm(raw_text)
        end_llm = time.time()
        print("Time cost of deepseek-V3: ", end_llm - start_llm)
        parsed_text, json_data = parse_refined_text(refined_text)
        # print(f"Parsed JSON: {json_data}")  # Debugging
    except Exception as e:
        return jsonify({"error": f"Text parsing failed: {str(e)}"}), 500

    # Return the results
    return jsonify({
        "raw_text": raw_text,
        "refined_text": parsed_text,
        "json_data": json_data
    })

if __name__ == "__main__":
    app.run(debug=True, port=8586)