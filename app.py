from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.utcnow()
    return render_template('index.html', browser_details=user_agent, access_time=current_time)
    # return response, user_agent, redirect


@app.route('/User/<name>')
def user(name):
    comments = {str(name), "goes", "to", "school"}
    return render_template('User.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_service_error(e):
    return render_template('500.html'), 500


@app.route('/Login')
def login():
    return render_template('Login.html')


@app.route('/Signup')
def signup():
    return render_template('Signup.html')


if __name__ == '__main__':
    app.run()
