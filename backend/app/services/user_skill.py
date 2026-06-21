from sqlalchemy.orm import Session

from app.repositories.user_skill import UserSkillRepository
from app.schemas.user_skill import UserSkillCreate

class UserSkillService:
    @staticmethod
    def get_all_user_skills(user_id: str, db: Session):
        user_skills = UserSkillRepository.get_all_user_skills(user_id, db)
        return {"data": user_skills}

    @staticmethod
    def create_user_skill(data: UserSkillCreate, db: Session):
        new_user_skill = UserSkillRepository.create_user_skill(data, db)
        return {"data": new_user_skill}