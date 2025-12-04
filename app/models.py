from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel

# Link Models
class UserArtistLink(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id", primary_key=True)

# Song Models
class SongBase(SQLModel):
    name: str
    duration: int
    album_id: int = Field(foreign_key="album.id")

class Song(SongBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    album: Optional["Album"] = Relationship(back_populates="songs")

class SongCreate(SongBase):
    pass

class SongRead(SongBase):
    id: int

# Album Models
class AlbumBase(SQLModel):
    name: str
    year: int
    artist_id: int = Field(foreign_key="artist.id")

class Album(AlbumBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artist: Optional["Artist"] = Relationship(back_populates="albums")
    songs: List[Song] = Relationship(back_populates="album")
    image_url: Optional[str] = Field(default=None)

class AlbumCreate(AlbumBase):
    pass

class AlbumRead(AlbumBase):
    id: int
    songs: List[SongRead] = []

# Artist Models
class ArtistBase(SQLModel):
    name: str
    genre: str

class Artist(ArtistBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    albums: List[Album] = Relationship(back_populates="artist")
    fans: List["User"] = Relationship(back_populates="favorite_artists", link_model=UserArtistLink)
    image_url: Optional[str] = Field(default=None)

class ArtistCreate(ArtistBase):
    pass

class ArtistRead(ArtistBase):
    id: int
    albums: List[AlbumRead] = []

# User Models
class UserBase(SQLModel):
    username: str
    email: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    favorite_artists: List[Artist] = Relationship(back_populates="fans", link_model=UserArtistLink)
    image_url: Optional[str] = Field(default=None)

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    favorite_artists: List[ArtistRead] = []
