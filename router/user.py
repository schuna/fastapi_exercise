from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from schema import UserBase, UserDisplay

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read user
@router.get('/{user_id}', response_model=UserDisplay)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, user_id)


# Update user
# noinspection PyShadowingBuiltins
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)


# Delete user
# noinspection PyShadowingBuiltins
@router.post('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
