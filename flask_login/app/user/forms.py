from unicodedata import name
from click import confirm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[ InputRequired()])
    username = StringField('Usuario', validators=[ InputRequired()])
    email = StringField('Email', validators=[ InputRequired()])
    password = StringField('password', validators=[ InputRequired(), EqualTo('confirm')])    
    confirm = StringField('Confirmar password', validators=[ InputRequired()]) 