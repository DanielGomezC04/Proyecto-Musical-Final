from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from ..database import get_session
from ..models import Album, AlbumCreate, AlbumRead

router = APIRouter(
    prefix="/albums",
    tags=["albums"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=AlbumRead)
def create_album(album: AlbumCreate, session: Session = Depends(get_session)):
    db_album = Album.model_validate(album)
    session.add(db_album)
    session.commit()
    session.refresh(db_album)
    return db_album

@router.get("/", response_model=List[AlbumRead])
def read_albums(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    albums = session.exec(select(Album).offset(offset).limit(limit)).all()
    return albums

@router.get("/{album_id}", response_model=AlbumRead)
def read_album(album_id: int, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album
