from sqlmodel import Session
from backend.films.ActorBackend import get_all_actors, getActorById
from models.actor_model import ActorDetailsView, ActorListView
from typing import List

from models.film_model import FilmListView

def fetchActors(session: Session) -> List[ActorListView]:
    actor_data = get_all_actors(session)
    print("######### Actors ", actor_data)
    return [
        ActorListView(
            actor_id=actor.actor_id,
            first_name =  actor.first_name,
            last_name = actor.last_name
        )
        for actor in actor_data
    ]

def fetchActorById(session: Session, id: int) -> ActorDetailsView:
    actor = getActorById(session, id)
    print("Fetched Actor", actor)

     # Extract list of films from film_actors
    films = [
        FilmListView(
            film_id=fa.film.film_id,
            title=fa.film.title,
            description=fa.film.description,
            release_year=fa.film.release_year
        )
        for fa in actor.film_actors if fa.film  # Make sure film is not None
    ]
    return ActorDetailsView(
        id=actor.actor_id,
        firstName = actor.first_name,
        lastName=actor.last_name,
        films=  films
        )
        
    
