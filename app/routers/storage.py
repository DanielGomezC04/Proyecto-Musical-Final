from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlmodel import Session, select
from ..database import get_session
from ..models import Artist, User, Album
from ..services.storage import StorageService

router = APIRouter(
    prefix="/storage",
    tags=["storage"]
)

@router.post("/upload/artist-image/{artist_id}")
async def upload_artist_image(
    artist_id: int,
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")

    # Generate unique filename
    filename = StorageService.generate_unique_filename(file.filename)
    path = f"{artist_id}/{filename}"
    
    # Upload to 'artist-images' bucket
    public_url = await StorageService.upload_file(file, "artist-images", path)
    
    # Update artist record
    artist.image_url = public_url
    session.add(artist)
    session.commit()
    session.refresh(artist)
    
    return {"image_url": public_url}

@router.post("/upload/profile-image/{user_id}")
async def upload_profile_image(
    user_id: int,
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    filename = StorageService.generate_unique_filename(file.filename)
    path = f"{user_id}/{filename}"
    
    # Upload to 'profile-images' bucket
    public_url = await StorageService.upload_file(file, "profile-images", path)
    
    user.profile_image_url = public_url
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return {"profile_image_url": public_url}

@router.post("/upload/album-cover/{album_id}")
async def upload_album_cover(
    album_id: int,
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    album = session.get(Album, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")

    filename = StorageService.generate_unique_filename(file.filename)
    path = f"{album_id}/{filename}"
    
    # Upload to 'album-covers' bucket
    public_url = await StorageService.upload_file(file, "album-covers", path)
    
    album.cover_image_url = public_url
    session.add(album)
    session.commit()
    session.refresh(album)
    
    return {"cover_image_url": public_url}

@router.post("/upload-url/artist-image/{artist_id}")
async def upload_artist_image_from_url(
    artist_id: int,
    image_url: str,
    session: Session = Depends(get_session)
):
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")

    # Generate unique filename
    filename = StorageService.generate_unique_filename("image.jpg") # Default extension, or could parse from URL
    path = f"{artist_id}/{filename}"
    
    # Upload to 'artist-images' bucket
    public_url = await StorageService.upload_from_url(image_url, "artist-images", path)
    
    # Update artist record
    artist.image_url = public_url
    session.add(artist)
    session.commit()
    session.refresh(artist)
    
    return {"image_url": public_url}

@router.post("/upload-url/profile-image/{user_id}")
async def upload_profile_image_from_url(
    user_id: int,
    image_url: str,
    session: Session = Depends(get_session)
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    filename = StorageService.generate_unique_filename("image.jpg")
    path = f"{user_id}/{filename}"
    
    # Upload to 'profile-images' bucket
    public_url = await StorageService.upload_from_url(image_url, "profile-images", path)
    
    user.profile_image_url = public_url
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return {"profile_image_url": public_url}

@router.post("/upload-url/album-cover/{album_id}")
async def upload_album_cover_from_url(
    album_id: int,
    image_url: str,
    session: Session = Depends(get_session)
):
    album = session.get(Album, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")

    filename = StorageService.generate_unique_filename("image.jpg")
    path = f"{album_id}/{filename}"
    
    # Upload to 'album-covers' bucket
    public_url = await StorageService.upload_from_url(image_url, "album-covers", path)
    
    album.cover_image_url = public_url
    session.add(album)
    session.commit()
    session.refresh(album)
    
    return {"cover_image_url": public_url}
