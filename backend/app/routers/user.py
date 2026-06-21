from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import CreateUser
from app.services.user import UserService

router = APIRouter()

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    res = UserService.get_all_users(db)
    return res

@router.get("/users/{user_id}")
def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    res = UserService.get_user_by_id(user_id, db)
    return res

@router.post("/users")
def create_user(data: CreateUser, db: Session = Depends(get_db)):
    res = UserService.create_user(data, db)
    return res
