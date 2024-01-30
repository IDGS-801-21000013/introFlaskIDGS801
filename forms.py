from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, TelField, EmailField, IntegerField
from wtforms import EmailField
# Aqui agregegaremos los campos que sean obligatorios y el email
from wtforms.validators import DataRequired, Email

class UserForm(Form):
    nombre=StringField("Nombre")    
    a_paterno=StringField("Apellido Paterno")
    a_materno=StringField("Apellido Materno")
    email=EmailField("Email")
    edad=IntegerField("Edad")




