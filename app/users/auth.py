from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from users.dao import UsersDAO


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def aware_utcnow():
    return datetime.now(timezone.utc)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = aware_utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, "akjgjfakghkfgahjkhg", "HS256"
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user


print(create_access_token({"data": "programmist"}))