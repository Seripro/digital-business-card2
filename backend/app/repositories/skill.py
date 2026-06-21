from sqlalchemy.orm import Session

from ..schemas.skill import SkillSearchRequest
from ..models.skill import Skill

class SkillRepository:
    @staticmethod
    def get_all_skills(data: SkillSearchRequest, db: Session):
        skills = (
            db.query(Skill)
            .filter(Skill.id.in_(data.skill_ids))
            .all()
        )
        return skills