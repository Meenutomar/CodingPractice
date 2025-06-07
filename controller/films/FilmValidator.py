from enum import Enum
from errors.BusinessException import BusinessException, YearException
from models.film_model import Film

class FilmValidator:

    @staticmethod
    def validate(film: Film):
        FilmValidator.validateRating(film.rating)
        FilmValidator.validateReleaseYear(film.release_year)
        FilmValidator.validateLength(film.length)
        FilmValidator.validateRentalDuration(film.rental_duration)

    @staticmethod
    def validateRating(rating):
       if rating not in FilmRating:
            raise BusinessException("Rating should be one of the following: PG, G, NC-17, R")
    
    @staticmethod
    def validateReleaseYear(year):
        if  year < 1975:
            raise YearException("Release year should be greater than 1975")
        
    @staticmethod
    def validateLength(length):
        if length < 100:
            raise BusinessException("Length should be greater than 100 minutes")
    
    @staticmethod
    def validateRentalDuration(rental_duration):
        if rental_duration >30:
            raise BusinessException("Rental duration should be less than or equal to 30 days")




class FilmRating(Enum):
    PG = "PG"
    G = "G"
    NC_17 = "NC-17"
    PG_13 = "PG-13"
    R = "R"


    