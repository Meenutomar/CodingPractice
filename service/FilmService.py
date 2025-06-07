from backend.films.FilmsBackend import get_all_films, getFilmById
from sqlmodel import Session
from models.film_model import FilmListView, FilmsDetailView,CategoryView
from typing import List


def fetchfilms(session: Session) -> List[FilmListView]:
    film_data = get_all_films(session)

    # Convert DB models to read models
    films: List[FilmListView] = [
        FilmListView(
            film_id=film.film_id,
            title=film.title,
            description=film.description,
            release_year=film.release_year
        )
        for film in film_data
    ]

    return films

def fetchFilmById(session: Session, id: int) -> FilmsDetailView:
    film = getFilmById(session, id)
    print("#################### Fetched Film:: for id:", id, film)

    categoriesList :List[CategoryView]=[
        CategoryView(
            name = filmCategory.category.name
        )
        for filmCategory in film.film_category
    ]  
    
    cat = []
    for category in categoriesList:
        cat.append(category.name)

    film_read = FilmsDetailView(
        film_id=film.film_id,
        title=film.title,
        description=film.description,
        release_year=film.release_year,
        rental_duration=film.rental_duration,
        language_id = film.language_id,
        length=film.length,
        rental_rate=film.rental_rate,
        replacement_cost=film.replacement_cost,
        rating=film.rating,
        last_update=film.last_update,
        original_language_id=film.original_language_id,
        categories = cat
    )

    return film_read


def createFilm(session, film):
    # Create a new film
    return ""
