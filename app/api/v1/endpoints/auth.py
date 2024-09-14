from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.schemas.token import Token
from app.services.user_service import user_service
from app.core.security import create_access_token
from app.db.session import get_db
from app.core.redis import redis_client
from app.core.config import settings
from datetime import timedelta

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, user_in.email, user_in.phone_number, user_in.password)
    if not user:
        raise HTTPException(status_code=400, detail="邮箱或手机号不存在，或密码错误")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=str(user.id), expires_delta=access_token_expires)
    redis_client.setex(access_token, settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60, str(user.id))
    return {"access_token": access_token, "token_type": "bearer"}
