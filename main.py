from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    escuela="UTL!!!"
    nombres=["Dario","Luis","Juan","Pedro"]
    return render_template("alumnos.html",escuela=escuela,nombres=nombres)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

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