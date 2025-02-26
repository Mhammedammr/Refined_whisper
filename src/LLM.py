import fireworks.client
# import openai
# import whisper
from groq import Groq
from dotenv import load_dotenv
import os

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

# def speech_reco(audio_file_path):
#     model = whisper.load_model("medium")  # Change to "tiny", "base", "medium" if needed
#     result = model.transcribe(audio_file_path, language="en")
#     print("speech_reco: ", result["text"])
#     return result["text"]


def llm(raw_text):
    # Set your Fireworks API key
    fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")

    # Define a prompt to refine the text
    prompt = f"""
        OpenAI Whisper text transcription: {raw_text}
        You are a medical assistant tasked with processing a text transcription generated by OpenAI Whisper from an audio file (e.g., a doctor-patient conversation or medical notes). Follow these steps:

        1. Refine the Text: (MUST be written)
        Improve the text grammatically and logically for better readability and coherence.
        Do not add any new words, sentences, or information not present in the original input.
        Ensure the refined text retains the original meaning and context.

        2. Extract Patient Features: (MUST be written)
        Extract the following key features of the patient and their medical history in a structured key-value JSON format:
        Diagnosis: The medical condition or diagnosis mentioned (refine the diagnosis with your medical information).
        ICD-10 Code: The ICD-10 code of the diagnosis (be strict to GET THE CLOSEST ICD 10 CODE from this website: "https://icd.who.int/browse10/2019/en#" (which is ICD 10 code version 2019), don't return any ICD 10 code that don't exist in the mentioned website).
        Gender: The gender of the patient.
        Age: The age of the patient.
        Smoker: boolean indicates smoking activivty for the patient.
        Medical History: Any relevant past medical history or conditions.
        Medications: any medications and drugs.
        Lab Tests: any lab tests.
        Imaging Studies: any imaging studies
        Signs and Symptoms: Any symptoms described by the patient or observed by the doctor.

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
            max_tokens=1000,  # Adjust based on the length of the text
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