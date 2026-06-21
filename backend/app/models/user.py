from sqlalchemy import Column, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    github_id = Column(String, index=True, nullable=True)
    qiita_id = Column(String, index=True, nullable=True)
    x_id = Column(String, index=True, nullable=True)