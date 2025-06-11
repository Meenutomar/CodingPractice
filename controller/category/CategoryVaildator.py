from enum import Enum

from sqlmodel import Session
from errors.BusinessException import BusinessException, NameException
from models.film_model import Category
from backend.category.category_backend import get_category_by_name
import logging as LOG

class CategoryValidator:

    @staticmethod
    def validate(category: Category, session: Session):
        CategoryValidator.validateName(category.name)
        CategoryValidator.validateLength(category.name)
        CategoryValidator.validateDuplicate(category.name, session)

    @staticmethod
    def validateName(name):
        if name == None or name == '':
            raise NameException("Name must be given")
        
    @staticmethod
    def validateLength(name):
        if len(name ) < 3:
            raise NameException("Name cantain atleast three letters")
  
    @staticmethod
    def validateDuplicate(name: str, session: Session):
        LOG.info("Validating Dupplicate Category name")
        category = get_category_by_name(name=name, session=session)
        if category:
            raise BusinessException("Category already exists")


    
    
   



    