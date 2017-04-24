from flask import render_template
from flask import request
from app import app
from app import db
from models import City
from models import Passenger
from models import Reservation
from models import Flight


@app.route('/')
def base():
    return render_template('base.html')

@app.route('/index/<flight_code>')
def index(flight_code):
    return render_template('index.html', category=Reservation.query.all(), flightCode=flight_code)


@app.route('/flights')
def flight():
    return render_template('flight.html', flight=Flight.query.all())


@app.route('/flights_check')
def check_flights():
    return render_template('check_flights.html', city=City.query.all())


@app.route('/check_results', methods=['GET', 'POST'])
def check_results():
    if request.method == 'POST':
        city_arrival = request.form.get('arrival')
        city_departure = request.form.get('departure')
    results = Flight.query.filter((Flight.city_arrival == city_arrival) and (Flight.city_departure == city_departure))
    return render_template('check_results.html', results=results)


@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        passenger = Passenger(first_name, last_name)
        db.session.add(passenger)
        db.session.commit()

        category_name = request.form.get('category')
        flight_code = request.form.get('flightCode')
        flight_filter = Flight.query.filter_by(flight_code=flight_code)

        for elem in flight_filter:
            flight_id = elem.flight_id

        reservation = Reservation(passenger.pass_id, flight_id, category_name)
        db.session.add(reservation)
        db.session.commit()

    return render_template('reservation_accepted.html', category=category_name, passenger=passenger, flight_code=flight_code)
