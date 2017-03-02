from flask import render_template
from flask import redirect
from flask import url_for
from flask import g
from flask_login import current_user
from app import app
from models import City
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    citys = City.query.all()

    user = { 'nickname': 'Miguel' }
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts, citys=citys)


@app.before_request
def before_request():
    g.user = None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)