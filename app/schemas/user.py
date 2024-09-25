from typing import Optional
from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

    @validator('email', 'phone_number', always=True)
    def validate_contact(cls, v, values, **kwargs):
        if not v and not values.get('email') and not values.get('phone_number'):
            raise ValueError('邮箱和手机号必须提供一个')
        return v


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    password: str

    @validator('email', 'phone_number', always=True)
    def validate_contact(cls, v, values, **kwargs):
        if not v and not values.get('email') and not values.get('phone_number'):
            raise ValueError('邮箱和手机号必须提供一个')
        return v
