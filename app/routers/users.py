from fastapi import APIRouter, Depends, HTTPException, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select
from typing import List, Optional
from pathlib import Path
from fastapi.templating import Jinja2Templates

from ..database import get_session
from ..models import User, UserCreate, UserRead, Artist, UserArtistLink, Song, UserSongLink
from ..utils import upload_image

# Configure templates
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# @router.post("/", response_model=UserRead)
# def create_user_api(user: UserCreate, session: Session = Depends(get_session)):
#     db_user = User.model_validate(user)
#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     return db_user

@router.get("/", response_class=HTMLResponse)
def read_users(request: Request, session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return templates.TemplateResponse("users/user_list.html", {"request": request, "users": users})

@router.get("/create", response_class=HTMLResponse)
def create_user_form(request: Request):
    return templates.TemplateResponse("users/user_create.html", {"request": request})

@router.post("/create", response_class=HTMLResponse)
async def create_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    file: UploadFile = File(None),
    session: Session = Depends(get_session)
):
    image_url = await upload_image(file, bucket_name="profile_images")
    user_data = UserCreate(username=username, email=email)
    db_user = User.model_validate(user_data)
    db_user.image_url = image_url
    
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    # Redirige a lista de usuarios
    return templates.TemplateResponse("users/user_detail.html", {"request": request, "user": db_user})

@router.get("/{user_id}", response_class=HTMLResponse)
def read_user(user_id: int, request: Request, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Fetch all artists and songs for the favorites dropdowns
    all_artists = session.exec(select(Artist)).all()
    all_songs = session.exec(select(Song)).all()
    
    return templates.TemplateResponse("users/user_detail.html", {
        "request": request, 
        "user": user,
        "all_artists": all_artists,
        "all_songs": all_songs
    })

@router.post("/{user_id}/favorites/{artist_id}", response_class=HTMLResponse)
def add_favorite_artist(user_id: int, artist_id: int, request: Request, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    
    if artist not in user.favorite_artists:
        user.favorite_artists.append(artist)
        session.add(user)
        session.commit()
        session.refresh(user)
    
    # Redirect to users list
    return read_users(request, session)

@router.delete("/{user_id}/favorites/{artist_id}", response_class=HTMLResponse)
def remove_favorite_artist(user_id: int, artist_id: int, request: Request, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    
    if artist in user.favorite_artists:
        user.favorite_artists.remove(artist)
        session.add(user)
        session.commit()
        session.refresh(user)
    
    # Redirect to users list
    return read_users(request, session)

@router.post("/{user_id}/favorites/{artist_id}/delete", response_class=HTMLResponse)
def delete_favorite_artist(user_id: int, artist_id: int, request: Request, session: Session = Depends(get_session)):
    """POST endpoint for deleting favorite artist (HTML form compatible)"""
    return remove_favorite_artist(user_id, artist_id, request, session)

@router.post("/{user_id}/favorites/songs/{song_id}", response_class=HTMLResponse)
def add_favorite_song(user_id: int, song_id: int, request: Request, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    
    if song not in user.favorite_songs:
        user.favorite_songs.append(song)
        session.add(user)
        session.commit()
        session.refresh(user)
    
    # Redirect to users list
    return read_users(request, session)

@router.post("/{user_id}/favorites/songs/{song_id}/delete", response_class=HTMLResponse)
def delete_favorite_song(user_id: int, song_id: int, request: Request, session: Session = Depends(get_session)):
    """POST endpoint for deleting favorite song (HTML form compatible)"""
    return remove_favorite_song(user_id, song_id, request, session)

@router.delete("/{user_id}/favorites/songs/{song_id}", response_class=HTMLResponse)
def remove_favorite_song(user_id: int, song_id: int, request: Request, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    
    if song in user.favorite_songs:
        user.favorite_songs.remove(song)
        session.add(user)
        session.commit()
        session.refresh(user)
    
    # Redirect to users list
    return read_users(request, session)





@router.post("/{user_id}/delete", response_class=HTMLResponse)
def delete_user(user_id: int, request: Request, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    session.delete(user)
    session.commit()
    
    # Redirect to user list
    return read_users(request, session)
