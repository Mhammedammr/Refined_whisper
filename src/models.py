import fireworks.client
from groq import Groq
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup

load_dotenv()

def speech_reco(audio_file_path):
    # Set your Groq API key
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))   
     
    # Open the audio file
    with open(audio_file_path, "rb") as file:
        # Create a transcription of the audio file
        transcription = client.audio.transcriptions.create(
        file=(audio_file_path, file.read()), # Required audio file
        model="whisper-large-v3-turbo", # Required model to use for transcription
        response_format="json",  # Optional
        language="en",  # Optional
        temperature=0.0  # Optional
        )
    # Print the transcription text
    return transcription.text


def llm(task, raw_text, html_text = None):
    # Set your Fireworks API key
    fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")
    if task == "voice":
        # Define a prompt to refine the text
        prompt = f"""
            OpenAI Whisper text transcription: {raw_text}
            You are a medical assistant tasked with processing a text transcription generated by OpenAI Whisper from an audio file (e.g., a doctor-patient conversation or medical notes). Follow these steps:

            1. Refine the Text: (MUST be written)
            Improve the text grammatically and logically for better readability and coherence.
            Do not add any new words, sentences, or information not present in the original input.
            Ensure the refined text retains the original meaning and context.

            2. Extract Patient Features: (MUST be written)
            Extract ONLY -be strict on that- the key features of the patient from the following HTML (html_text) in a structured key-value JSON format:
            {html_text}

            3. Reasoning: (MUST be written)
            write your reasons here.
            

            please be strict to the above structure and write the title before (MUST be written) before any section.

            If a specific feature is not mentioned in the input, assign the value null
            to that key (except ICD10 code).
            make sure the output message to be written with the sentence that have (MUST be written) message and be free in any format.
            Explain your reasoning step by step before providing the answer .
            """

        # Call the Fireworks DeepSeek API
        try:
            response = fireworks.client.Completion.create(
                model="accounts/fireworks/models/deepseek-v3",  # Use the correct model name
                prompt=prompt,
                max_tokens=100000,  # Adjust based on the length of the text
                temperature=0.3,  # Lower temperature for more deterministic output
            )
            # Extract the refined text
            if response.choices and response.choices[0].text.strip():
                refined_text = response.choices[0].text.strip()
                # print("refined_text: ", refined_text)
            else:
                print("No text generated by the model. Falling back to raw text.")
                refined_text = raw_text  # Fallback to raw text if no output is generated

            # print("Refined Text:", refined_text)
            return refined_text
        except Exception as e:
            print(f"Error in LLM function: {e}")
            return raw_text  # Fallback to raw text if an error occurs
        
    else:
        soup = BeautifulSoup(raw_text, "html.parser")

        # Remove unnecessary tags
        for tag in soup(["script", "style", "meta", "link", "head"]):
            tag.decompose()

        cleaned_html = soup.prettify()
        # Define a prompt to refine the text
        prompt = f"""
            HTML input: {cleaned_html}
            DeepSeek-V3, please analyze the provided HTML -clincal sheets- input and 
            extract all the key features related to the patient in that HTML format. 
            Ensure the extracted information is structured in a clear and concise format,
            such as a JSON object.
            make sure that JSON output is not nested JSON is just key (description of key) to value (text or number or boolean).
            make sure that the key value output to be related to medical domain as you can.
            """

        # Call the Fireworks DeepSeek API
        try:
            response = fireworks.client.Completion.create(
                model="accounts/fireworks/models/deepseek-v3",  # Use the correct model name
                prompt=prompt,
                max_tokens=100000,  # Adjust based on the length of the text
                temperature=0.3,  # Lower temperature for more deterministic output
            )
            # Extract the refined text
            if response.choices and response.choices[0].text.strip():
                json_features = response.choices[0].text.strip()
                # print("refined_text: ", refined_text)
            else:
                print("No feature extracted.")

            # print("Refined Text:", refined_text)
            return json_features
        except Exception as e:
            print(f"Error in LLM function: {e}")
            return raw_text  # Fallback to raw text if an error occurs