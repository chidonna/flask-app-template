from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import EqualTo, Required


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    password2 = PasswordField(
        'Confirm Password', validators=[Required(),
                                        EqualTo('password')])
    submit = SubmitField('Register')
