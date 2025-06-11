from typing import Optional, List
from sqlmodel import Field, PrimaryKeyConstraint, SQLModel, Relationship
from pydantic import BaseModel
import datetime
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from models.actor_model import Film_Actor

class Film_Category(SQLModel,table = True):
    category_id: int = Field(foreign_key= "category.category_id")
    film_id: int = Field(foreign_key="film.film_id")

    film: Optional["Film"] = Relationship(back_populates="film_category")
    category: Optional["Category"] = Relationship(back_populates="film_category")

    __table_args__ = (
        PrimaryKeyConstraint("category_id", "film_id"),
    )


class Category(SQLModel,table = True):
    category_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    film_category: List["Film_Category"] = Relationship(back_populates="category")


class Film(SQLModel, table=True):
    film_id: Optional[int] = Field(default=None, primary_key=True)
    title: str 
    description: Optional[str]
    release_year: Optional[int]
    language_id: int
    original_language_id: Optional[int]
    rental_duration: int
    rental_rate: float
    length: Optional[int]
    replacement_cost: float
    rating: Optional[int]
    last_update: datetime.datetime
    # special_features: str
    # fulltext: str

    # Relationship to Film_Actor
    film_actors: List["Film_Actor"] = Relationship(back_populates="film")
    film_category: List[Film_Category] = Relationship(back_populates="film")


class FilmRead(BaseModel):
    film_id: int
    title: str
    description: str
    release_year: int
    language_id: int
    original_language_id: Optional[int]
    rental_duration: Optional[int]
    rental_rate: Optional[float]
    length: Optional[int]
    replacement_cost: Optional[float]
    rating: str
    last_update: datetime.datetime
    # special_features: str
    # fulltext: str


class FilmListView(BaseModel):
    film_id: int
    title: str
    description: str
    release_year: int

class CategoryView(BaseModel):
    #id: Optional[int]
    name: str


class FilmsDetailView(BaseModel):
    film_id: int
    title: str
    description: Optional[str]
    release_year: Optional[int]
    language_id: Optional[int]
    original_language_id: Optional[int]
    rental_duration: Optional[int]
    rental_rate: Optional[float]
    length: Optional[int]
    replacement_cost: Optional[float]
    rating: str
    last_update: datetime.datetime
    categories: List[str]
    # special_features: str
    # fulltext: str


class ActorModel(BaseModel) :
    id: int
    name: str

class FilmsCreateModel(BaseModel):
    film_id: Optional[int]= None
    title: str
    description: Optional[str] = None
    release_year: Optional[int] = None
    language_id: Optional[int] = None
    original_language_id: Optional[int] = None
    rental_duration: Optional[int] = None
    rental_rate: Optional[float] = None
    length: Optional[int] = None
    replacement_cost: Optional[float] = None
    rating: str
    actors: List[ActorModel]
    categories: List[str]

