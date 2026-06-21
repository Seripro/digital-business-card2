from sqlalchemy.orm import Session

from app.schemas.user_skill import UserSkillCreate
from app.models.user_skill import UserSkill


class UserSkillRepository:
    @staticmethod
    def get_all_user_skills(user_id: str, db: Session):
        user_skills = db.query(UserSkill).filter_by(user_id=user_id).all()
        return user_skills

    @staticmethod
    def create_user_skill(data: UserSkillCreate, db: Session):
        new_user_skill = UserSkill(user_id=data.user_id, skill_id=data.skill_id)
        db.add(new_user_skill)
        db.commit()
        db.refresh(new_user_skill)
        return new_user_skill
