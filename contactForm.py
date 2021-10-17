from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('What is your full name?', validators=[DataRequired()])
    nickname = StringField("Nickname??", validators=[DataRequired()])
    email = StringField("Input your email address!!", validators=[DataRequired()])
    password = PasswordField("Set your password!!", validators=[DataRequired()])
    submit = SubmitField('Submit')
