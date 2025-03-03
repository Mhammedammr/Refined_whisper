import json
import re

def parse_refined_text(input_text):
    """
    Parse input text to separate refined text and JSON data.
    Args:
        input_text (str): Input text containing both refined text and JSON data
    Returns:
        tuple: (refined_text, json_data, reasoning) where:
            - refined_text (str): The extracted refined text
            - json_data (dict): The parsed JSON data
            - reasoning (str): The reasoning text (if available)
    """
    # Split the text into parts using the numbered sections
    parts = input_text.split("2. Extract Patient Features: (MUST be written)")
    if len(parts) != 2:
        raise ValueError("Input text does not contain the expected format")
    
    # Extract and clean the refined text
    refined_text_part = parts[0].replace("1. Refine the Text: (MUST be written)", "").replace("1. Refined Text:", "").strip()
    
    # Check if there's a reasoning section and split accordingly
    if "3. Reasoning: (MUST be written)" in parts[1]:
        part_of_parts = parts[1].split("3. Reasoning: (MUST be written)")
        json_text = part_of_parts[0].strip()
        reasoning = part_of_parts[1].strip() if len(part_of_parts) > 1 else ""
    else:
        json_text = parts[1].strip()
        reasoning = ""
    
    # Remove the ```json and ``` markers if they exist
    json_text = re.sub(r'```json\s*|\s*```', '', json_text)
    
    # Clean up the JSON string
    json_text = json_text.strip()

    
    try:
        # Parse the JSON data
        json_data = json.loads(json_text)
    except json.JSONDecodeError as e:
        # Provide more context for debugging
        print(f"JSONDecodeError: {str(e)}")
        print(f"Problematic JSON Text: {json_text}")
        raise ValueError(f"Failed to parse JSON data: {str(e)}")
    
    return refined_text_part, json_data, reasoning