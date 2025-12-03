from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from ..database import get_session
from ..models import Artist, ArtistCreate, ArtistRead

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

@router.get("/", response_model=List[ArtistRead])
def read_artists(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    artists = session.exec(select(Artist).offset(offset).limit(limit)).all()
    return artists

@router.get("/{artist_id}", response_model=ArtistRead)
def read_artist(artist_id: int, session: Session = Depends(get_session)):
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist
