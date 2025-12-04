import cloudinary
import cloudinary.uploader
from fastapi import UploadFile
from .config import get_settings

settings = get_settings()

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.cloudinary_cloud_name,
    api_key=settings.cloudinary_api_key,
    api_secret=settings.cloudinary_api_secret
)

async def upload_image(file: UploadFile, bucket_name: str = "images") -> str:
    """
    Upload image to Cloudinary.
    bucket_name parameter is used as folder name in Cloudinary.
    """
    if not file:
        return None
    
    try:
        # Read file content
        file_content = await file.read()
        
        # Upload to Cloudinary with folder organization
        result = cloudinary.uploader.upload(
            file_content,
            folder=bucket_name,
            resource_type="auto"
        )
        
        # Return the secure URL
        return result.get('secure_url')
    except Exception as e:
        print(f"Error uploading to Cloudinary: {e}")
        return None
