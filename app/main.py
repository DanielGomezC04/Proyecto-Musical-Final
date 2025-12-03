from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import create_db_and_tables
from .routers import users, artists, albums, songs

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.include_router(artists.router)
app.include_router(albums.router)
app.include_router(songs.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Proyecto Musical"}
