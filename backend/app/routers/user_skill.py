from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user_skill import UserSkillCreate
from app.services.user_skill import UserSkillService

router = APIRouter()

@router.get("/user_skill/{user_id}")
def get_all_user_skills(user_id: str, db: Session = Depends(get_db)):
    res = UserSkillService.get_all_user_skills(user_id, db)
    return res

@router.post("/user_skill")
def create_user_skill(data: UserSkillCreate, db: Session = Depends(get_db)):
    res = UserSkillService.create_user_skill(data, db)
    return res
