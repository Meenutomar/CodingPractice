from fastapi import APIRouter, Depends
from backend.databasepaglu import get_session_pagli
from models.film_model import FilmListView, FilmsDetailView
from service.FilmService import  fetchfilms,fetchFilmById,FilmsDetailView
from sqlmodel import Session
from typing import List

router = APIRouter()

@router.get("/films", response_model=List[FilmListView])
def read_films(session: Session = Depends(get_session_pagli)):
    return fetchfilms(session)

@router.get("/films/{id}", response_model=FilmsDetailView)
def get_film_by_id(id: int, session: Session = Depends(get_session_pagli)):
    print("Fetching Film by ID: ", id)
    return fetchFilmById(session, id)
