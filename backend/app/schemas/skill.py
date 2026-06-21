from pydantic import BaseModel

class SkillSearchRequest(BaseModel):
    skill_ids: list[int]