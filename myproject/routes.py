# myproject/routes.py
from flask import jsonify, request, Blueprint
from myproject import app, db
from .models import Flight, Booking, Passenger
from .schemas import user_schema
from wtforms import ValidationError
import datetime, uuid 

api = Blueprint('api', __name__)

@api.route('/search_flights', methods=['GET'])
def search_flights():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    departure_date = datetime.datetime.fromisoformat(request.args.get('date'))
    flights = Flight.query.filter_by(origin=origin, destination=destination, departure_time=departure_date).all()
    return jsonify([flights.as_dict() for flight in flights])

@api.route('/create_bookings', methods=['POST'])
def book_flight():
    data = request.get_json()

    # 1. Validate user data
    try:
        user_data = user_schema.load({
            "first_name" : data["first_name"],
            "last_name" : data["last_name"],
            "date_of_birth" : data["date_of_birth"],
            "gender": data["gender"],
            "email": data["email"],
            "phone_number": data["phone_number"]
        })
    except ValidationError as err:
        return jsonify({"status": "error", "errors": err.messages}), 400
    

    # 2. Check if user exists
    user = Passenger.query.filter_by(email=data['email']).first()
    if not user:
        # User doesn't exist; Create new user
        user = Passenger(**user_data)
        db.session.add(user)
        db.session.commit()

    # 3. Validate flight ID exists
    flight = Flight.query.get(data["flight_id"])
    if not flight:
        return jsonify({"status": "error", "message": "Flight not found"}), 404

    # 4. Generate a unique booking reference
    booking_reference_u = str(uuid.uuid4())[:8].upper()

    # 5. Finally, save booking information
    booking = Booking(
        passenger_id= user.passenger_id,
        passenger_email=user.email, 
        passenger_first_name=user.first_name,
        passenger_last_name=user.last_name, 
        flight_id= data['flight_id'], 
        seat_number=data['seat_number'],
        booking_reference=booking_reference_u # Use generated booking reference from above
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({"status": "success", "message": "Success! Your booking was created.", "booking_reference":booking.booking_reference}), 201


@api.route('/view_bookings', methods=['GET'])
def view_bookings(user_id):
    # Retrieve query parameters
    email = request.args.get('email')
    booking_reference = request.args.get('booking_reference')
    last_name = request.args.get('last_name')

    # Validate required parameters
    if not last_name or not ((email and last_name) or (booking_reference and last_name)):
        return jsonify({"status": "error", "message": "Provide either email and last name, or booking reference and last name"}), 400

    # Search based on email and last name
    if email:
        user = Passenger.query.filter_by(email=email).first()
        if not user or user.last_name != last_name:
            return jsonify({"status": "error", "message": "No user found with provided email and last name"}), 404
        bookings = Booking.query.filter_by(passenger_last_name=user.last_name).all()
    # OR Search based on booking reference and last name 
    else:
        bookings = Booking.query.filter_by(booking_reference=booking_reference).all()
        if not bookings or bookings[0].passenger_last_name != last_name:
            return jsonify({"status": "error", "message": "No booking found with provided booking reference and last name"}), 404
     
    # If there are bookings, return findings
    bookings_data = [{
        "booking_reference": booking.booking_reference,
        "flight_id": booking.flight_id,
        "passenger_first_name": booking.passenger_first_name,
        "passenger_last_name": booking.passenger_last_name,
        "booking_date": booking.booking_date,
        "seat_number": booking.seat_number
    } for booking in bookings]

    return jsonify({"status": "success", "bookings": bookings_data})

@api.route('/passengers', methods=['POST'])
def add_passenger():
    data = request.get_json()

    # 1. Validate user data
    try:
        new_passenger_data = user_schema.load({
            "first_name" : data["first_name"],
            "last_name" : data["last_name"],
            "date_of_birth" : data["date_of_birth"],
            "gender": data["gender"],
            "email": data["email"],
            "phone_number": data["phone_number"]
        })
    except ValidationError as err:
        return jsonify({"status": "error", "errors": err.messages}), 400
    
    # 2. Check if user exists
    passenger = Passenger.query.filter_by(email=data['email']).first()
    if not passenger:
        # User doesn't exist; Create new user
        passenger = Passenger(**new_passenger_data)
        db.session.add(passenger)
        db.session.commit()