import os

from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from contactForm import ContactForm
from loginForm import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf ;lkj'
bootstrap = Bootstrap(app)
moment = Moment(app)


current_time = datetime.utcnow()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', browser_details=user_agent, access_time=current_time)
    # return response, user_agent, redirect


@app.route('/User/<name>')
def user(name):
    comments = {str(name), "goes", "to", "school"}
    return render_template('User.html', name=name, access_time=current_time)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', access_time=current_time), 404


@app.errorhandler(500)
def internal_service_error(e):
    return render_template('500.html', access_time=current_time), 500


@app.route('/Login', methods=['GET', 'POST'])
def login():
    nick = None
    password = None
    form = LoginForm()
    if form.validate_on_submit():
        nick = form.nickname.data
        form.nickname.data = ''
        password = form.password.data
        form.password.data = ''
    return render_template('Login.html', form=form, access_time=current_time)


@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    name = None
    nickname = None
    email = None
    password = None
    form = ContactForm()
    if form.validate_on_submit():
        nickname = form.nickname.data
        form.nickname.data = ''
        name = form.name.data
        form.name.data = ''
        password = form.password.data
        form.password.data = ''
    return render_template('Signup.html', form=form, access_time=current_time)


if __name__ == '__main__':
    app.run()
