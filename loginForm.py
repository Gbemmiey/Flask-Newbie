from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    nickname = StringField("Nickname??", validators=[DataRequired()])
    password = PasswordField("Set your password!!", validators=[DataRequired()])
    submit = SubmitField('Submit')