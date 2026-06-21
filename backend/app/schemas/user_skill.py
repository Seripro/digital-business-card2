from pydantic import BaseModel


class UserSkillCreate(BaseModel):
    user_id: str
    skill_id: int
    