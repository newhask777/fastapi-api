-- SELECT * FROM public.bookings WHERE room_id=1
-- ORDER BY id ASC 

WITH booked_rooms AS (
	SELECT * FROM bookings
	WHERE room_id = 1 AND
	(date_from >= '2033-11-01' AND date_from <= '2033-11-05') OR
	(date_from <= '2033-11-01' AND date_to > '2033-11-01')
)

SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
WHERE rooms.id = 1
GROUP BY rooms.quantity
