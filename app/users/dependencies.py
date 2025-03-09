from fastapi import Depends, Request, status
from jose import jwt, JWTError

from exceptions import IncorectTokenFormatException, TokenAbsentException, TokenExpiredException, UserDataException, UserPermissionsException
from users.models import Users
from users.auth import utcnow
from users.dao import UsersDAO
from config import settings


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    # print(request.url)
    # print(request.client)
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorectTokenFormatException

    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < utcnow().timestamp()):
        raise TokenExpiredException
 
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserDataException
    
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
         raise UserDataException
    
    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    # if current_user.role != "admin":
    #     raise UserPermissionsException
    return current_user