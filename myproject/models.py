# myproject/models.py
from flask import Flask, jsonify, request
from myproject import db
from datetime import datetime
from sqlalchemy.orm import relationship

class Flight(db.Model):
    __tablename__ = 'flights'
    flight_id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20))
    origin = db.Column(db.String(50))
    destination = db.Column(db.String(50))
    flight_date = db.Column(db.Date)
    departure_time = db.Column(db.Time)
    arrival_time = db.Column(db.Time)
    available_seats = db.Column(db.Integer)
    duration=db.Column(db.Integer)
    price = db.Column(db.Float)

    def __init__(self, flight_number, origin, destination, flight_date, departure_time, arrival_time, available_seats, duration, price):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.flight_date = flight_date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.available_seats = available_seats
        self.duration = duration
        self.price = price
    
    # def __repr__(self):
    #     return f"Flight {self.flight_number} is set to leave from {self.origin} to {self.destination} on {self.flight_date}.\n"

    def to_dict(self):
        # Combine time with flight date for consistency
        departure_datetime = datetime.combine(self.flight_date, self.departure_time)
        arrival_datetime = datetime.combine(self.flight_date, self.arrival_time)

        return {
            'flight_number': self.flight_number,
            'origin': self.origin,
            'destination': self.destination,
            'flight_date': self.flight_date.strftime('%Y-%m-%d'),  # Ensure flight_date is a date object
            'departure_time': departure_datetime.strftime('%H:%M:%S'),  # Formatted time
            'arrival_time': arrival_datetime.strftime('%H:%M:%S'),  # Formatted time
            'duration': str(self.duration),  # Convert duration to string
            'available_seats': self.available_seats,
            'price': self.price
        }

class Passenger(db.Model):
    __tablename__ = 'passengers'
    passenger_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100),  unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    bookings=db.relationship('Booking', backref='passenger', lazy=True)

    def __init__(self, first_name, last_name, date_of_birth, gender, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.phone_number = phone_number


class Booking(db.Model):
    __tablename__ = 'bookings'
    booking_id = db.Column(db.Integer, primary_key=True)
    passenger_id = db.Column(db.Integer, db.ForeignKey('passengers.passenger_id'))
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'))
    seat_number = db.Column(db.String(10))
    booking_date = db.Column(db.DateTime, default = datetime.now)
    booking_reference = db.Column(db.String(100), unique=True)
    passenger_first_name = db.Column(db.String(20), nullable=False)
    passenger_last_name = db.Column(db.String(20), nullable=False)
    passenger_email = db.Column(db.String(100))

    def __init__(self, passenger_id, flight_id, booking_date, booking_reference, passenger_first_name, passenger_last_name, passenger_email, seat_number):
        self.passenger_id = passenger_id
        self.flight_id = flight_id
        self.booking_date = booking_date
        self.booking_reference = booking_reference
        self.passenger_first_name = passenger_first_name
        self.passenger_last_name = passenger_last_name
        self.passenger_email = passenger_email
        self.seat_number = seat_number

class Seats(db.Model):
    __tablename__ = 'seats'
    seat_id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String)

    def __init__(self, seat_number):
        self.seat_number = seat_number