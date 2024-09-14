from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password
from typing import Optional


class UserService:
    def get_user(self, db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    def create_user(self, db: Session, user_in: UserCreate) -> User:
        if user_in.email and db.query(User).filter(User.email == user_in.email).first():
            raise HTTPException(status_code=400, detail="邮箱已被注册")
        if user_in.phone_number and db.query(User).filter(User.phone_number == user_in.phone_number).first():
            raise HTTPException(status_code=400, detail="手机号已被注册")
        hashed_password = get_password_hash(user_in.password)
        user = User(
            email=user_in.email,
            phone_number=user_in.phone_number,
            hashed_password=hashed_password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update_user(self, db: Session, user_id: int, user_in: UserUpdate) -> User:
        user = self.get_user(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="用户不存在")
        if user_in.email:
            user.email = user_in.email
        if user_in.phone_number:
            user.phone_number = user_in.phone_number
        if user_in.password:
            user.hashed_password = get_password_hash(user_in.password)
        db.commit()
        db.refresh(user)
        return user

    def delete_user(self, db: Session, user_id: int):
        user = self.get_user(db, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="用户不存在")
        db.delete(user)
        db.commit()

    def authenticate_user(self, db: Session, email: Optional[str], phone_number: Optional[str], password: str) -> Optional[User]:
        if email:
            user = db.query(User).filter(User.email == email).first()
        elif phone_number:
            user = db.query(User).filter(User.phone_number == phone_number).first()
        else:
            return None
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user


user_service = UserService()
