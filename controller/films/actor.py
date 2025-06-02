from fastapi import APIRouter, Depends
from backend.databasepaglu import get_session_pagli
from models.actor_model import ActorDetailsView, ActorListView
from sqlmodel import Session
from typing import List
from service.ActorService import fetchActorById, fetchActors

router = APIRouter()

@router.get("/actors", response_model=List[ActorListView])
def read_actors(session: Session = Depends(get_session_pagli)):
    return fetchActors(session)

@router.get("/actors/{id}", response_model=ActorDetailsView)
def actor_by_id(id: int, session: Session = Depends(get_session_pagli)):
    print("Fetching Actor by ID: ", id)
    return fetchActorById(session, id)
