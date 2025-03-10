from fastapi import HTTPException, status


UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already exists!",
)


IncorectUserEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=" Incorrect user email or password!",
)


TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token is expire!",
)


TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Auth token was not found!",
)


IncorectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect token format!",
)


UserDataException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect user data",
)


UserPermissionsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Permissions error!",
)


RoomCannotBeBooked = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="All rooms are booked!"
)