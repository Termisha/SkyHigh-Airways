from myproject import db, app
from myproject.models import Flight, Passenger, Seats
from datetime import datetime

with app.app_context():
    db.create_all()

    # Already executed
    # BWA1513 = Flight('BWA1513', 'TAB', 'POS', datetime(2024,11,2,11,37), datetime(2024,11,2,12,00), 20, 200)
    # BWA237 = Flight('BWA237', 'SVD', 'BGI', datetime(2024,11,2,11,46), datetime(2024,11,2,12,14), 20, 300)
    # BWA432 = Flight('BWA432', 'POS', 'GND', datetime(2024,11,2,11,58), datetime(2024,11,2,12,8), 20, 400)
    # BWA484 = Flight('BWA484', 'POS', 'MIA', datetime(2024,11,2,9,9), datetime(2024,11,2,11,44), 30, 1000)
    # BWA79 = Flight('BWA79', 'KIN', 'YYZ', datetime(2024,11,2,11,37), datetime(2024,11,2,14,00), 30, 700)

    # db.session.add_all([BWA1513, BWA237, BWA432, BWA484, BWA79])
    # db.session.commit()

    # print(BWA1513.flight_id)
    # print(BWA237.flight_id)

    # Allison = Passenger('Allison', 'Gates', datetime(2000,10,1), 'Female', 'alison.gates@hotmail.com', 8681234567)
    # Henry = Passenger('Henry', 'Phillip', datetime(1990,10,1), 'Male', 'henry.phillip@hotmail.com', 8681234567)
    # db.session.add_all([Allison, Henry])
    # db.session.commit()

    # Anna = Passenger('Anna', 'Daly', datetime(1990,10,1), 'Female', 'anna.daly@hotmail.com', 8681234567)
    # db.session.add(Anna)
    # db.session.commit()
    # print(Anna.passenger_id)


    # A1 = Seats('1A')
    # db.session.add(A1)
    # db.session.commit()
    # B1 = Seats('1B')
    # A2 = Seats('2A')
    # B2 = Seats('2B')
    # A3 = Seats('3A')
    # B3 = Seats('3B')
    # A4 = Seats('4A')
    # B4 = Seats('4B')
    # A5 = Seats('5A')
    # B5 = Seats('5B')
    # db.session.add_all([B1,A2,B2,A3,B3,A4,B4,A5,B5])
    # db.session.commit()
    # print(B5.seat_id, B5.seat_number)


    # BWA1500 = Flight('BWA1513', 'POS', 'JFK', datetime(2024,11,12,11,37), datetime(2024,11,12,12,00), 20, 1200)
    # db.session.add(BWA1500)
    # db.session.commit()
    # print(BWA1500.flight_id)
    # print(Flight.query.all())