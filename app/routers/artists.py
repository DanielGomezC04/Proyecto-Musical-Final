from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select
from typing import List
from pathlib import Path
from fastapi.templating import Jinja2Templates

from ..database import get_session
from ..models import Artist, ArtistCreate, ArtistRead

# Configure templates
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))

router = APIRouter(
    prefix="/artists",
    tags=["artists"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ArtistRead)
def create_artist(artist: ArtistCreate, session: Session = Depends(get_session)):
    db_artist = Artist.model_validate(artist)
    session.add(db_artist)
    session.commit()
    session.refresh(db_artist)
    return db_artist

@router.get("/", response_class=HTMLResponse)
def read_artists(request: Request, session: Session = Depends(get_session)):
    artists = session.exec(select(Artist)).all()
    return templates.TemplateResponse("artists/artist_list.html", {"request": request, "artists": artists})

@router.get("/create", response_class=HTMLResponse)
def create_artist_form(request: Request):
    return templates.TemplateResponse("artists/artist_create.html", {"request": request})

@router.post("/create", response_class=HTMLResponse)
def create_artist(
    request: Request,
    name: str = Form(...),
    genre: str = Form(...),
    session: Session = Depends(get_session)
):
    artist_data = ArtistCreate(name=name, genre=genre)
    db_artist = Artist.model_validate(artist_data)
    
    session.add(db_artist)
    session.commit()
    session.refresh(db_artist)

    return templates.TemplateResponse("artists/artist_detail.html", {"request": request, "artist": db_artist})

@router.get("/{artist_id}", response_class=HTMLResponse)
def read_artist(artist_id: int, request: Request, session: Session = Depends(get_session)):
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return templates.TemplateResponse("artists/artist_detail.html", {"request": request, "artist": artist})


