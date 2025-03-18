import os
from groq import Groq

class SpeechService:
    """Service for speech recognition."""
    
    @staticmethod
    def transcribe_audio(audio_file_path, api_key):
        """Transcribe audio file to text."""
        client = Groq(api_key=api_key)
        
        try:
            with open(audio_file_path, "rb") as file:
                transcription = client.audio.transcriptions.create(
                    file=(audio_file_path, file.read()),
                    model="whisper-large-v3-turbo",
                    response_format="json",
                    language="en",
                    temperature=0.0
                )
            return transcription.text
        except Exception as e:
            raise Exception(f"Audio transcription failed: {str(e)}")