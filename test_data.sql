INSERT INTO hotels (name, location, services, rooms_quantity, image_id) VALUES
('Sunset Paradise Resort', 'Miami, Florida', '["wifi", "pool", "spa"]', 120, 101),
('Mountain Peak Lodge', 'Aspen, Colorado', '["wifi", "gym"]', 80, 102),
('Ocean Breeze Hotel', 'San Diego, California', '["wifi", "pool", "gym", "spa"]', 150, 103),
('Golden Sands Inn', 'Myrtle Beach, South Carolina', '["wifi", "pool"]', 90, 104),
('Royal Crown Plaza', 'New York City, New York', '["wifi", "pool", "gym", "spa", "restaurant"]', 200, 105),
('Emerald Valley Retreat', 'Portland, Oregon', '["wifi", "spa"]', 60, 106);

INSERT INTO rooms (hotel_id, name, description, price, quantity, services, image_id) VALUES
(1, 'Deluxe Suite', 'A luxurious suite with a king-sized bed, ocean view, and modern amenities.', 250, 10, '["wifi", "tv", "minibar", "room_service"]', 201),
(1, 'Standard Room', 'A comfortable room with a queen-sized bed and essential amenities.', 150, 20, '["wifi", "tv"]', 202),
(2, 'Mountain View Suite', 'A spacious suite with breathtaking mountain views and a cozy fireplace.', 300, 5, '["wifi", "tv", "fireplace", "balcony"]', 203),
(2, 'Cozy Cabin', 'A rustic cabin with a warm fireplace and a serene forest view.', 200, 15, '["wifi", "tv", "fireplace"]', 204),
(3, 'Ocean View Room', 'A bright room with stunning ocean views and a private balcony.', 350, 8, '["wifi", "tv", "minibar", "balcony"]', 205),
(3, 'Family Suite', 'A large suite perfect for families, featuring a sofa bed and extra space.', 400, 6, '["wifi", "tv", "minibar", "sofa_bed"]', 206),
(4, 'Beachfront Room', 'A room with direct access to the beach and a private balcony.', 280, 12, '["wifi", "tv", "balcony"]', 207),
(4, 'Economy Room', 'A budget-friendly room with all the essential amenities.', 120, 25, '["wifi", "tv"]', 208),
(5, 'Executive Suite', 'An elegant suite with a jacuzzi, perfect for business or leisure travelers.', 500, 4, '["wifi", "tv", "minibar", "jacuzzi"]', 209),
(5, 'Presidential Suite', 'The ultimate luxury experience with a jacuzzi, butler service, and panoramic views.', 800, 2, '["wifi", "tv", "minibar", "jacuzzi", "butler_service"]', 210),
(6, 'Forest Retreat Room', 'A peaceful room surrounded by nature, perfect for relaxation.', 180, 10, '["wifi", "tv", "balcony"]', 211);

INSERT INTO users (email, hashed_password) VALUES
('john.doe@example.com', 'hashed_password_123'),
('jane.smith@example.com', 'hashed_password_456'),
('alice.wonderland@example.com', 'hashed_password_789');

INSERT INTO bookings (room_id, user_id, date_from, date_to, price) VALUES
(1, 1, '2023-11-01', '2023-11-05', 1000),
(2, 2, '2023-11-10', '2023-11-15', 750),
(3, 3, '2023-12-01', '2023-12-07', 1800),
(4, 1, '2023-12-20', '2023-12-25', 1200),
(5, 2, '2024-01-05', '2024-01-10', 1750);