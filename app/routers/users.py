from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select
from typing import List
from pathlib import Path
from fastapi.templating import Jinja2Templates

from ..database import get_session
from ..models import User, UserCreate, UserRead, Artist, UserArtistLink

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
def create_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    session: Session = Depends(get_session)
):
    user_data = UserCreate(username=username, email=email)
    db_user = User.model_validate(user_data)
    
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
    return templates.TemplateResponse("users/user_detail.html", {"request": request, "user": user})

@router.post("/{user_id}/favorites/{artist_id}", response_model=UserRead)
def add_favorite_artist(user_id: int, artist_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    
    
    if artist in user.favorite_artists:
        return user

    user.favorite_artists.append(artist)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.delete("/{user_id}/favorites/{artist_id}", response_model=UserRead)
def remove_favorite_artist(user_id: int, artist_id: int, session: Session = Depends(get_session)):
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
        
    return user




