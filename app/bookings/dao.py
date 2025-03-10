from datetime import date
from sqlalchemy import and_, func, insert, or_, select
from hotels.models import Rooms
from dao.base import BaseDAO
from bookings.models import Bookings
from database import async_session_maker, engine


class BookingDAO(BaseDAO): # Data access object or service or repo
    model = Bookings
   

    @classmethod
    async def add(cls, user_id: int, room_id: int, date_from: date, date_to: date):
        """
            WITH booked_rooms AS (
                SELECT * FROM bookings
                WHERE room_id = 1 AND
                (date_from >= '2033-11-01' AND date_from <= '2033-11-05') OR
                (date_from <= '2033-11-01' AND date_to > '2033-11-01')
            )

            SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
            LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
            WHERE rooms.id = 1
            GROUP BY rooms.quantity, booked_rooms.room_id
        """
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == 1,
                    or_(
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_from <= date_to
                        ),
                        and_(
                            Bookings.date_from <= date_from,
                            Bookings.date_to > date_from
                        )
                    )
                )
            ).cte("booked_rooms")

            get_rooms_left = select((Rooms.quantity - func.count(booked_rooms.c.room_id)).label("rooms_left")).select_from(Rooms).join(
                booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
            ).where(Rooms.id == 1).group_by(
                Rooms.quantity, booked_rooms.c.room_id
            )

            # print(get_rooms_left.compile(engine, compile_kwargs={"literal_binds": True}))

            rooms_left = await session.execute(get_rooms_left)
            rooms_left: int = rooms_left.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar() 

                add_booking = insert(Bookings).values(room_id=room_id, user_id=user_id, date_from=date_from, date_to=date_to, price=price
                                                      ).returning(Bookings)
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
            else:
                return None


