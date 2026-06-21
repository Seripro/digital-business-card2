from sqlalchemy.orm import Session

from app.schemas.skill import SkillSearchRequest
from app.repositories.skill import SkillRepository

class SkillService:
    @staticmethod
    def get_all_skills(data: SkillSearchRequest, db: Session):
        skills = SkillRepository.get_all_skills(data, db)
        return {"data": skills}