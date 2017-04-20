from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index=True, unique=True)
    user_email = db.Column(db.String(120), index=True, unique=True)
    user_role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __repr__(self):
        return '<User {0}>'.format(self.login)


class Passenger(db.Model):
    pass_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Flight(db.Model):
    flight_id = db.Column(db.Integer, primary_key=True)
    flight_code = db.Column(db.VARCHAR, unique=True)
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    city_arrival = db.Column(db.String, db.ForeignKey('city.city_name'))
    city_departure = db.Column(db.String, db.ForeignKey('city.city_name'))


class City(db.Model):
    city_name = db.Column(db.String(64), primary_key=True)
    country = db.Column(db.String(64))


class Reservation(db.Model):
    reserv_id = db.Column(db.Integer, primary_key=True)
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.pass_id'))
    reserv_flight = db.Column(db.Integer, db.ForeignKey('flight.flight_id'))
    reserv_class = db.Column(db.String(64))
    seat_number = db.Column(db.String(10))

    def __init__(self, passenger_id, reserv_flight, reserv_class):
        self.passenger_id = passenger_id
        self.reserv_flight = reserv_flight
        self.reserv_class = reserv_class