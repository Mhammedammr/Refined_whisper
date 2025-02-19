from flask import Flask, request, jsonify, render_template
from src.LLM import llm, speech_reco
import os

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

    # Save the uploaded file
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_file.filename)
    audio_file.save(file_path)

    # Transcribe the audio
    try:
        raw_text = speech_reco(file_path)
        refined_text = llm(raw_text)
        return jsonify({"raw_text": raw_text, "refined_text": refined_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)