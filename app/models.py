from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

# Tabla de asociación para Many-to-Many entre User y Artist (Favoritos)
class UserArtistLink(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id", primary_key=True)

class SongBase(SQLModel):
    title: str
    duration: int # en segundos

class Song(SongBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
    album: Optional["Album"] = Relationship(back_populates="songs")

class SongCreate(SongBase):
    pass

class SongRead(SongBase):
    id: int


class AlbumBase(SQLModel):
    title: str
    year: int

class Album(AlbumBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id")
    artist: Optional["Artist"] = Relationship(back_populates="albums")
    songs: List[Song] = Relationship(back_populates="album")

class AlbumCreate(AlbumBase):
    pass

class AlbumRead(AlbumBase):
    id: int
    songs: List[SongRead] = []


class ArtistBase(SQLModel):
    name: str
    genre: str

class Artist(ArtistBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    albums: List[Album] = Relationship(back_populates="artist")
    favorited_by: List["User"] = Relationship(back_populates="favorite_artists", link_model=UserArtistLink)

class ArtistCreate(ArtistBase):
    pass

class ArtistRead(ArtistBase):
    id: int
    albums: List[AlbumRead] = []


class UserBase(SQLModel):
    username: str
    email: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    favorite_artists: List[Artist] = Relationship(back_populates="favorited_by", link_model=UserArtistLink)

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    favorite_artists: List[ArtistRead] = []
