# myproject/models.py
from flask import Flask, jsonify, request
from myproject import db
import datetime

class Flight(db.Model):
    __tablename__ = 'flights'
    flight_id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20))
    origin = db.Column(db.String(50))
    destination = db.Column(db.String(50))
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    available_seats = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __init__(self, flight_number, origin, destination, departure_time, arrival_time, available_seats, price):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.available_seats = available_seats
        self.price = price
    
    def __repr__(self):
        return f"Flight {self.flight_number} is set to leave from {self.origin} to {self.destination}."


class Passenger(db.Model):
    __tablename__ = 'passengers'
    passenger_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(100),  unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    bookings=db.relationship('Booking', backref='user', lazy=True)

    def __init__(self, first_name, last_name, dob, gender, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = dob
        self.gender = gender
        self.email = email
        self.phone_number = phone


class Booking(db.Model):
    __tablename__ = 'bookings'
    booking_id = db.Column(db.Integer, primary_key=True)
    passenger_id = db.Column(db.Integer, db.ForeignKey('passengers.passenger_id'))
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'))
    seat_number = db.Column(db.String(10))
    booking_date = db.Column(db.DateTime, default = datetime.datetime.now)
    booking_reference = db.Column(db.String(100), unique=True)
    passenger_first_name = db.Column(db.String(20), nullable=False)
    passenger_last_name = db.Column(db.String(20), nullable=False)
    passenger_email = db.Column(db.String(100))

class Seats(db.Model):
    __tablename__ = 'seats'
    seat_id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String)

    def __init__(self, seat_number):
        self.seat_number = seat_number