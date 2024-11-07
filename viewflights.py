from myproject import db, app
from myproject.models import Flight
from datetime import date

with app.app_context():
    db.create_all()
    
    # print(Flight.query.all())

    # fli = Flight.query.get(1)
    # fli.date = date(2024,11,12)
    # db.session.add(fli)
    # db.session.commit()

    flights = Flight.query.filter_by(origin='Chicago',
        destination='Miami',
        flight_date=date(2024, 11, 11)).all()
    print(flights)

    # flighttime = Flight.query.filter_by(date="2024-11-2").all()
    # print(flighttime)