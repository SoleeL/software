from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class RegistroForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message="Campo requerido"), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired(message="Campo requerido")])
    email = StringField('Email', validators=[DataRequired(message="Campo requerido"), Email()])
    submit = SubmitField('Registrar')
