import cloudinary
import cloudinary.uploader
from fastapi import UploadFile, HTTPException
from ..config import get_settings
import uuid
import os
import httpx

settings = get_settings()

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.cloudinary_cloud_name,
    api_key=settings.cloudinary_api_key,
    api_secret=settings.cloudinary_api_secret
)

class StorageService:
    @staticmethod
    async def upload_file(file: UploadFile, folder: str = "daniel_project") -> str:
        """
        Upload a file to Cloudinary and return its secure URL.
        """
        try:
            # Read file content
            file_content = await file.read()
            
            # Upload to Cloudinary
            result = cloudinary.uploader.upload(
                file_content,
                folder=folder,
                resource_type="auto"
            )
            
            return result.get("secure_url")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to upload file to Cloudinary: {str(e)}")

    @staticmethod
    async def upload_from_url(url: str, folder: str = "daniel_project") -> str:
        """
        Upload a file from a URL to Cloudinary.
        """
        try:
            result = cloudinary.uploader.upload(
                url,
                folder=folder,
                resource_type="auto"
            )
            return result.get("secure_url")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to upload from URL: {str(e)}")

    @staticmethod
    def delete_file(public_id: str):
        """
        Delete a file from Cloudinary using its public_id.
        Note: The public_id is usually the path without the extension and version.
        """
        try:
            cloudinary.uploader.destroy(public_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to delete file: {str(e)}")

    @staticmethod
    def generate_unique_filename(original_filename: str) -> str:
        # Cloudinary handles unique naming, but keeping this for compatibility if needed
        extension = os.path.splitext(original_filename)[1]
        return f"{uuid.uuid4()}{extension}"
