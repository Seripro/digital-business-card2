from sqlalchemy import Column, Integer, String
from app.database import Base

class UserSkill(Base):
    __tablename__ = "user_skill"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    skill_id = Column(Integer, index=True)