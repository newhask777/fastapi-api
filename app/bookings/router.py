from fastapi import APIRouter
from bookings.schemas import SBooking
from database import async_session_maker
from bookings.dao import BookingDAO
 
router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingDAO.find_all(room_id=1)
 

