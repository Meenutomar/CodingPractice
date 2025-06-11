from typing import List
from sqlmodel import Session
from models.category_model import CategoryCreateModel, CategoryView
from models.film_model import Category
from backend.category.category_backend import get_all_category,get_category_by_id, create_category
import logging as LOG

def fetchCategory(session: Session) -> List[str]:
    category_data = get_all_category(session)
    category: List[str] = [
            category.name
        for category in category_data
    ]
    return category


def createCategory( session, category: CategoryCreateModel):
    LOG.info(f'Entering Service Layer: {category}')
    try:
        new_Category = Category(
            name=category.name
            )
        create_category(session, new_Category)
        session.commit()
    except Exception as e:
        LOG.error(f'Error creating category: {e}')
    finally:
        session.close()
        LOG.info(f'Exiting create category')
    
    





