from fastapi import APIRouter, Depends, HTTPException
from backend.databasepaglu import get_session_pagli
from controller.films.FilmValidator import FilmValidator
from errors.TechnicalException import TechnicalException
from errors.BusinessException import BusinessException
from models.film_model import FilmListView, FilmsDetailView,FilmsCreateView
from service.FilmService import  fetchfilms,fetchFilmById, createFilm

from sqlmodel import Session
from typing import List

router = APIRouter()

@router.post("/films", tags=["films"])
def create_film(film: FilmsCreateView, session: Session = Depends(get_session_pagli)):
    print("Inside Create Films::", film)
    try:
        FilmValidator.validate(film)
        return createFilm(session=session,film=film)
        
    except BusinessException as be:
        raise HTTPException(be.code, be.message)
    except TechnicalException as te:
        raise HTTPException(te.code, te.message)
    
    #return ""

@router.get("/films", response_model=List[FilmListView])
def read_films(session: Session = Depends(get_session_pagli)):
    try:
        return fetchfilms(session)
    except TechnicalException as te:
        raise HTTPException(te.code, te.message)

@router.get("/films/{id}", response_model=FilmsDetailView)
def get_film_by_id(id: int, session: Session = Depends(get_session_pagli)):
    print("Fetching Film by ID: ", id)
    return fetchFilmById(session, id)
