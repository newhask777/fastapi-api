from fastapi import APIRouter, Depends, Request
from users.dependencies import get_current_user
from users.models import Users
from bookings.schemas import SBooking
from database import async_session_maker
from bookings.dao import BookingDAO
 
router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)): #-> list[SBooking]:
    #print(user, type(user), user.email)
    return await BookingDAO.find_all(user_id=user.id)
 
 