from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render your HTML form

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Process text input if present
        if 'text' in request.form and request.form['text'].strip():
            text_input = request.form['text'].strip()
            print("Text input received:", text_input)
            # Process the text here
        else:
            print("No text input received")
        
        # Process audio file if present
        if 'audio' in request.files and request.files['audio'].filename:
            audio_file = request.files['audio']
            print("Audio file received:", audio_file.filename)
            # Process the audio file here
            # For example: audio_file.save(os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename))
        else:
            print("No audio file received")
        
        # Make sure at least one input was provided
        if ('text' not in request.form or not request.form['text'].strip()) and \
           ('audio' not in request.files or not request.files['audio'].filename):
            return jsonify({"success": False, "error": "No input provided"}), 400
        
        # Continue with your processing logic here
        
        return jsonify({"success": True, "message": "Data processed successfully"})
    
    except Exception as e:
        print(f"Error processing form: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)