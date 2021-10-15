from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', browser_details=user_agent)
    # return response, user_agent, redirect


@app.route('/user/<name>')
def user(name):
    comments = {str(name), "goes", "to", "school"}
    return render_template('User.html', name=name, comments=comments)


if __name__ == '__main__':
    app.run()
