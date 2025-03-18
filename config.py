import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration."""
    UPLOAD_FOLDER = "uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
    ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg'}
    
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")

    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:7987@localhost:5432/Voice_Recognition")

    
    # Create upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)