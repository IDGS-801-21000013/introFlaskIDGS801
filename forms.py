from wtforms import Form
from wtforms import StringField, TelField, EmailField

class UserForm(Form):
    nombre=StringField("Nombre")
    email=StringField("Email") #Crear campo de validacion correcto
    a_paterno=StringField("Apellido Paterno")