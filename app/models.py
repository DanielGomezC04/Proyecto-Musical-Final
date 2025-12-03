from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

# Tabla de asociación para Many-to-Many entre User y Artist (Favoritos)
class UserArtistLink(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id", primary_key=True)

class SongBase(SQLModel):
    title: str
    artist_name: str

class Song(SongBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
    album: Optional["Album"] = Relationship(back_populates="songs")

class SongCreate(SongBase):
    album_id: Optional[int] = None

class SongRead(SongBase):
    id: int
    album_id: Optional[int] = None


class AlbumBase(SQLModel):
    title: str
    year: int

class Album(AlbumBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cover_image_url: Optional[str] = None
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id")
    artist: Optional["Artist"] = Relationship(back_populates="albums")
    songs: List[Song] = Relationship(back_populates="album")

class AlbumCreate(AlbumBase):
    artist_id: Optional[int] = None

class AlbumRead(AlbumBase):
    id: int
    cover_image_url: Optional[str] = None
    artist_id: Optional[int] = None
    songs: List[SongRead] = []


class ArtistBase(SQLModel):
    name: str
    genre: str

class Artist(ArtistBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    image_url: Optional[str] = None
    albums: List[Album] = Relationship(back_populates="artist")
    favorited_by: List["User"] = Relationship(back_populates="favorite_artists", link_model=UserArtistLink)

class ArtistCreate(ArtistBase):
    pass

class ArtistRead(ArtistBase):
    id: int
    image_url: Optional[str] = None
    albums: List[AlbumRead] = []


class UserBase(SQLModel):
    username: str
    email: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    profile_image_url: Optional[str] = None
    favorite_artists: List[Artist] = Relationship(back_populates="favorited_by", link_model=UserArtistLink)

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    profile_image_url: Optional[str] = None
    favorite_artists: List[ArtistRead] = []
