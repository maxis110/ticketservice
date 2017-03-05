from flask import render_template
from flask import request
from app import app
from models import City
from models import Flight


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/flights')
def flight():
    return render_template('flight.html', flight=Flight.query.all())


@app.route('/check')
def check_flights():
    return render_template('check_flights.html', city=City.query.all())


@app.route('/check_results', methods=['GET', 'POST'])
def check_results():
    if request.method == 'POST':
        arrival = request.form.get('arrival')
        departure = request.form.get('departure')
    results = Flight.query.filter((Flight.city_arrival == arrival) and (Flight.city_departure == departure))
    return render_template('check_results.html', results=results)
