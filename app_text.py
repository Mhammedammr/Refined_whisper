from flask import Flask, request, jsonify, render_template
import time
import logging
from config import Config
from services.llm_service import LLMService
from services.text_parser import parse_refined_text

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index_html():
    """Render the application frontend."""
    return render_template("index_text.html")

@app.route("/upload", methods=["POST"])
def upload():
    """Handle file uploads and processing."""
    form_text = request.form.get('text', '')
    input_text = request.form.get('text2', '')
    
    try:
        # Process the uploaded file
        process_start_time = time.time()
        
        # Step 1: Process the HTML input text
        json_data = LLMService.process_html_data(
            form_text,
            app.config["FIREWORKS_API_KEY"]
        )
        process_HTML_time = time.time() - process_start_time
        logging.info(f"Time taken to process HTML: {process_HTML_time:.4f} seconds")
        
        # Step 2: Process the transcription with LLM
        text_start_time = time.time()
        refined_text = LLMService.process_text_data(
            input_text, 
            json_data,
            app.config["FIREWORKS_API_KEY"]
        )
        extract_time = time.time() - text_start_time
        logging.info(f"Time taken to process text with LLM: {extract_time:.4f} seconds")
        
        print(refined_text)

        # Step 3: Parse the refined text
        json_data, reasoning = parse_refined_text(refined_text)

        processing_time = time.time() - process_start_time
        logging.info(f"the Total Processing time: {processing_time:.4f} seconds")

        print(json_data)
        
        # Return the results
        return jsonify({
            "json_data": json_data,
            "reasoning": reasoning,
        })
    
    except Exception as e:
        logging.error(f"Error processing upload: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8587)
