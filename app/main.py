from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .database import create_db_and_tables
from .routers import users, artists, albums, songs, storage

# Configure templates
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.include_router(artists.router)
app.include_router(albums.router)
app.include_router(songs.router)
app.include_router(storage.router)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
