from flask import Flask, render_template, request
from forms import UserForm

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    # escuela="UTL!!!"
    # nombres=["Dario","Luis","Juan","Pedro"]
    # return render_template("alumnos.html",escuela=escuela,nombres=nombres)
    
    alumno_clase = UserForm(request.form)
    nombre = None
    a_paterno = None
    a_materno = None
    email = None
    edad = None
    
    if request.method == "POST" and alumno_clase.validate():
        nombre = alumno_clase.nombre.data
        a_paterno = alumno_clase.a_paterno.data
        a_materno = alumno_clase.a_materno.data
        email = alumno_clase.email.data
        edad = alumno_clase.edad.data
        
        print(f"Nombre: {nombre} {a_paterno} {a_materno} Email: {email} Edad: {edad}")

    return render_template("alumnos.html",form=alumno_clase,nombre=nombre,a_paterno=a_paterno,a_materno=a_materno,email=email,edad=edad)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/calcular", methods=["GET","POST"])
def calcular():
    if request.method == "POST":
        n1=int(request.form["n1"])
        n2=int(request.form["n2"])
        return f"La multiplicacion de {n1} * {n2} es {n1*n2}"
    return '''
    <form action="/calcular" method="POST">
        <label for="n1">Numero 1</label> 
        <input type="text" name="n1"> <br>
        <label for="n2">Numero 2</label>
        <input type="text" name="n2"> <br>
        <input type="submit" value="Enviar">
    </form> 
    '''

@app.route("/OperasBas")
def operaciones():
    return render_template("operasBas.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        n1=int(request.form["n1"])
        n2=int(request.form["n2"])
        return f"La multiplicacion de {n1} * {n2} es {n1*n2}"

@app.route("/hola")
def hola():
    return "<h1>Hola mundo</h1>"

@app.route("/saludo")
def saludo():
    return "<h1>Saludos</h1>"

@app.route("/nombre/<string:nombre>")
def nombre(nombre):
    return "<h1>Hola {}</h1>".format(nombre)


@app.route("/numero/<int:n1>")
def num(n1):
    return f"<h1>Numero: {n1}</h1>"

@app.route("/user/<int:n1>/<string:nombre>")
def user(n1, nombre):
    return f"<h1>ID: {n1}  Nombre: {nombre}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma de {n1} y {n2} es {n1+n2}</h1>"

@app.route("/default")
@app.route("/default/<string:d>")
def default(d="Dario"):
    return "El nombre de usuario es: "+d





if __name__ == "__main__":
    app.run(debug=True) 