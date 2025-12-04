from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select
from typing import List
from pathlib import Path
from fastapi.templating import Jinja2Templates

from ..database import get_session
from ..models import Song, SongCreate, SongRead, Album

# Configure templates
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=SongRead)
def create_song(song: SongCreate, session: Session = Depends(get_session)):
    db_song = Song.model_validate(song)
    session.add(db_song)
    session.commit()
    session.refresh(db_song)
    return db_song

@router.get("/", response_class=HTMLResponse)
def read_songs(request: Request, session: Session = Depends(get_session)):
    songs = session.exec(select(Song)).all()
    return templates.TemplateResponse("songs/song_list.html", {"request": request, "songs": songs})

@router.get("/create", response_class=HTMLResponse)
def create_song_form(request: Request, session: Session = Depends(get_session)):
    albums = session.exec(select(Album)).all()
    return templates.TemplateResponse("songs/song_create.html", {"request": request, "albums": albums})

@router.post("/create", response_class=HTMLResponse)
def create_song(
    request: Request,
    name: str = Form(...),
    duration: int = Form(...),
    album_id: int = Form(...),
    session: Session = Depends(get_session)
):
    song_data = SongCreate(name=name, duration=duration, album_id=album_id)
    db_song = Song.model_validate(song_data)
    
    session.add(db_song)
    session.commit()
    session.refresh(db_song)

    return templates.TemplateResponse("songs/song_detail.html", {"request": request, "song": db_song})

@router.get("/{song_id}", response_class=HTMLResponse)
def read_song(song_id: int, request: Request, session: Session = Depends(get_session)):
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return templates.TemplateResponse("songs/song_detail.html", {"request": request, "song": song})


