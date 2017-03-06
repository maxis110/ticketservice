from flask import render_template
from flask import request
from app import app
from app import db
from models import City
from models import Category
from models import Passenger
from models import Reservation
from models import Flight


@app.route('/')
@app.route('/index/<flightCode>')
def index(flightCode):
    return render_template('index.html', category=Category.query.all(), flightCode=flightCode)


@app.route('/flights')
def flight():
    return render_template('flight.html', flight=Flight.query.all())


@app.route('/check')
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
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        passenger = Passenger(firstname, lastname)
        db.session.add(passenger)
        db.session.commit()

        categoryName = request.form.get('category')
        categoryFilter = Category.query.filter_by(categ_name=categoryName)
        for category in categoryFilter:
            category_id = category.categ_id

        flightCode = request.form.get('flightCode')
        flightFilter = Flight.query.filter_by(flight_code=flightCode)
        for elem in flightFilter:
            flight_id = elem.flight_id
        reservation = Reservation(passenger.pass_id, flight_id, category_id)
        db.session.add(reservation)
        db.session.commit()

    return render_template('reservation_accepted.html', category=categoryName, passenger=passenger, flight_id=flight_id)
