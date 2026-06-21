from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.skill import SkillSearchRequest
from app.services.skill import SkillService

router = APIRouter()

@router.post("/skills")
def get_all_skills(data: SkillSearchRequest, db: Session = Depends(get_db)):
    records = SkillService.get_all_skills(data, db)
    return records
