import os
import uuid

class FileService:
    """Service for file handling."""
    
    @staticmethod
    def save_file(file, upload_folder):
        """Save uploaded file with a unique filename."""
        unique_filename = FileService._generate_unique_filename(file.filename)
        file_path = os.path.join(upload_folder, unique_filename)
        
        try:
            file.save(file_path)
            return file_path
        except Exception as e:
            raise Exception(f"Failed to save file: {str(e)}")
    
    @staticmethod
    def cleanup_file(file_path):
        """Remove a file from the filesystem."""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            raise Exception(f"Failed to clean up file: {str(e)}")
    
    @staticmethod
    def _generate_unique_filename(filename):
        """Generate a unique filename."""
        unique_id = uuid.uuid4().hex
        _, ext = os.path.splitext(filename)
        return f"{unique_id}{ext}"