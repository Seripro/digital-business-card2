from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import CreateUser

class UserRepository:
    @staticmethod
    def get_all_users(db: Session):
        users = db.query(User).all()
        return users
    
    @staticmethod
    def get_user_by_id(user_id: str, db: Session):
        user = db.query(User).filter_by(user_id=user_id).first()
        return user
    
    @staticmethod
    def create_user(data: CreateUser, db: Session):
        new_user = User(user_id=data.user_id, name=data.name, description=data.description, github_id=data.github_id, qiita_id=data.qiita_id, x_id=data.x_id)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user