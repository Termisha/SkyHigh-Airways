from datetime import date, time
from myproject import db, app
from myproject.models import Flight

# Sample flight data
flights = [
    Flight(
        flight_number='AA101',
        origin='New York',
        destination='Los Angeles',
        flight_date=date(2024, 11, 10),
        departure_time=time(8, 30),  # 08:30 AM
        arrival_time=time(11, 45),  # 11:45 AM
        duration='6h 15m',
        available_seats=20,
        price=299.99
    ),
    Flight(
        flight_number='AA102',
        origin='Los Angeles',
        destination='Chicago',
        flight_date=date(2024, 11, 10),
        departure_time=time(13, 0),  # 01:00 PM
        arrival_time=time(19, 15),  # 07:15 PM
        duration='4h 15m',
        available_seats=20,
        price=199.99
    ),
    Flight(
        flight_number='UA203',
        origin='Chicago',
        destination='Miami',
        flight_date=date(2024, 11, 11),
        departure_time=time(9, 0),  # 09:00 AM
        arrival_time=time(12, 30),  # 12:30 PM
        duration='3h 30m',
        available_seats=20,
        price=179.99
    ),
    Flight(
        flight_number='DL150',
        origin='Miami',
        destination='New York',
        flight_date=date(2024, 11, 12),
        departure_time=time(15, 30),  # 03:30 PM
        arrival_time=time(18, 30),  # 06:30 PM
        duration='3h 0m',
        available_seats=20,
        price=220.00
    ),
    Flight(
        flight_number='UA310',
        origin='San Francisco',
        destination='Dallas',
        flight_date=date(2024, 11, 15),
        departure_time=time(7, 45),  # 07:45 AM
        arrival_time=time(12, 30),  # 12:30 PM
        duration='4h 45m',
        available_seats=20,
        price=249.99
    ),
    Flight(
        flight_number='AA400',
        origin='Dallas',
        destination='Boston',
        flight_date=date(2024, 11, 16),
        departure_time=time(10, 0),  # 10:00 AM
        arrival_time=time(13, 0),  # 01:00 PM
        duration='3h 0m',
        available_seats=20,
        price=189.99
    ),
    Flight(
        flight_number='DL560',
        origin='Boston',
        destination='San Francisco',
        flight_date=date(2024, 11, 17),
        departure_time=time(16, 0),  # 04:00 PM
        arrival_time=time(19, 30),  # 07:30 PM
        duration='6h 30m',
        available_seats=20,
        price=329.99
    ),
    Flight(
        flight_number='UA725',
        origin='New York',
        destination='Miami',
        flight_date=date(2024, 11, 18),
        departure_time=time(11, 30),  # 11:30 AM
        arrival_time=time(14, 30),  # 02:30 PM
        duration='3h 0m',
        available_seats=20,
        price=249.99
    )
]

with app.app_context():
    db.create_all()
    # Add sample flights to the database
    for flight in flights:
        db.session.add(flight)

    # Commit the changes to the database
    db.session.commit()

    print(flights)