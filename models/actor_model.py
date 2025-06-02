from datetime import date
from typing import Optional, List
from sqlmodel import Field, PrimaryKeyConstraint, SQLModel, Relationship
from typing import TYPE_CHECKING
from models.film_model import FilmListView

if TYPE_CHECKING:
    from models.film_model import Film

class Actor(SQLModel, table=True):
    actor_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    #last_update: time
    # Relationship to Film_Actor
    film_actors: List["Film_Actor"] = Relationship(back_populates="actor")

    
class Film_Actor(SQLModel, table=True):
    #__name__="film_actor"
    #id: Optional[int] = Field(default=None, primary_key=True)
    actor_id: int = Field(foreign_key= "actor.actor_id")
    film_id: int = Field(foreign_key="film.film_id")
    last_update: date

    # Relationship to Film
    film: Optional["Film"] = Relationship(back_populates="film_actors")
    actor: Optional["Actor"] = Relationship(back_populates="film_actors")

    __table_args__ = (
        PrimaryKeyConstraint("actor_id", "film_id"),
    )

    


class ActorListView(SQLModel):
    actor_id: int
    first_name: str
    last_name: str
    
class ActorDetailsView(SQLModel):
    id: int
    firstName: str
    lastName: str
    films: List[FilmListView]
   # last_update: date

    class Config:
        orm_mode = True
