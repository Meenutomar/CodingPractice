from unicodedata import category
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from backend.databasepaglu import get_session_pagli
from controller.category.CategoryVaildator import CategoryValidator
from errors.BusinessException import BusinessException
from errors.TechnicalException import TechnicalException
from models.category_model import CategoryCreateModel
from models.film_model import CategoryView
from service.CategoryService import createCategory, fetchCategory
import logging as LOG

router = APIRouter()


@router.post("/categories", tags=["categories"])
def create_category(category: CategoryCreateModel, session: Session = Depends(get_session_pagli)):
    LOG.info(f'Entering Create Category: {category}')
    try:
        CategoryValidator.validate(category, session)
        
        createCategory(session=session,category=category)
        return {"message": "Category created successfully"}
        
    except BusinessException as be:
        raise HTTPException(be.code, be.message)
    except TechnicalException as te:
        raise HTTPException(te.code, te.message)
    finally:
         LOG.info("Exiting Create Category")
    

@router.get("/categories", response_model=List[str])
def read_films(session: Session = Depends(get_session_pagli)):
    try:
        return fetchCategory(session)
    except TechnicalException as te:
        raise HTTPException(te.code, te.message)

