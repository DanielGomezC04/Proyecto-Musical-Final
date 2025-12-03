import os
from supabase import create_client, Client
import httpx
from fastapi import UploadFile, HTTPException
from ..config import get_settings
import uuid

settings = get_settings()

# Initialize Supabase client
supabase: Client = create_client(settings.supabase_url, settings.supabase_key)

class StorageService:
    @staticmethod
    async def upload_file(file: UploadFile, bucket: str, path: str) -> str:
        """
        Upload a file to Supabase Storage and return its public URL.
        """
        try:
            file_content = await file.read()
            # Upload file to Supabase
            # file_options={"content-type": file.content_type} is optional but good practice
            res = supabase.storage.from_(bucket).upload(
                path=path,
                file=file_content,
                file_options={"content-type": file.content_type}
            )
            
            # Get public URL
            public_url = supabase.storage.from_(bucket).get_public_url(path)
            return public_url
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")

    @staticmethod
    async def upload_from_url(url: str, bucket: str, path: str) -> str:
        """
        Download a file from a URL and upload it to Supabase Storage.
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                if response.status_code != 200:
                    raise HTTPException(status_code=400, detail="Failed to download image from URL")
                
                file_content = response.content
                content_type = response.headers.get("content-type", "image/jpeg") # Default to jpeg if unknown

            # Upload to Supabase
            res = supabase.storage.from_(bucket).upload(
                path=path,
                file=file_content,
                file_options={"content-type": content_type}
            )
            
            # Get public URL
            public_url = supabase.storage.from_(bucket).get_public_url(path)
            return public_url
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to process URL upload: {str(e)}")

    @staticmethod
    def get_public_url(bucket: str, path: str) -> str:
        return supabase.storage.from_(bucket).get_public_url(path)

    @staticmethod
    def delete_file(bucket: str, path: str):
        try:
            supabase.storage.from_(bucket).remove([path])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to delete file: {str(e)}")

    @staticmethod
    def generate_unique_filename(original_filename: str) -> str:
        extension = os.path.splitext(original_filename)[1]
        return f"{uuid.uuid4()}{extension}"
