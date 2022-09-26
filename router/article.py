from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_article
from db.database import get_db
from schema import ArticleBase, ArticleDisplay, UserBase
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/article',
    tags=['article']
)


# Create
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db),
                   current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)


# Get
@router.get('/{id}')
def get_article(id: int, db: Session = Depends(get_db),
                current_user: UserBase = Depends(get_current_user)):
    return {
        'data': db_article.get_article(db, id),
        'current_user': current_user
    }


@router.post("/{id}/update")
def update_article(id: int, request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.update_article(db, id, request)


@router.post("/delete/{id}")
def delete_article(id: int, db: Session = Depends(get_db)):
    return db_article.delete_article(db, id)
