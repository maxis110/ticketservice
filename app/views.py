from flask import render_template
from flask import redirect
from flask import url_for
from flask import g
from app import app
from models import City
from models import Flight
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    city = City.query.all()
    return render_template('index.html', city=city)


@app.route('/flights')
def flight():
    flight = Flight.query.all()
    duration = []
    for elem in flight:
        duration.append(elem.arrival_time - elem.departure_time)

    print duration
    print flight

    return render_template('flight.html', flight=flight, duration=duration)


@app.before_request
def before_request():
    g.user = None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)