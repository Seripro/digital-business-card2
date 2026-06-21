from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.user import CreateUser

class UserService:
    @staticmethod
    def get_all_users(db: Session):
        users = UserRepository.get_all_users(db)
        return {"data": users}
    
    @staticmethod
    def get_user_by_id(user_id: str, db: Session):
        user = UserRepository.get_user_by_id(user_id, db)
        return {"data": user}
    
    @staticmethod
    def create_user(data: CreateUser, db: Session):
        user = UserRepository.create_user(data, db)
        return {"data": user}