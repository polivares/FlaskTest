# Importing flask library
from flask import Flask, render_template, request

# Creating an instance of flask app
app = Flask(__name__)

# Routes
@app.route("/home")
@app.route("/")
def index():
    num = ["a", "b", "c", "d", "e"]
    return render_template("index.html", num=num)

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/hola/<string:nombre>")
def hola(nombre):
    return f"<h1> Hola {nombre} </h1>"

# Form test
@app.route("/getmensaje", methods=["POST"])
def getmensaje():
    nombre = request.form.get("nombre")
    return render_template("getmensaje.html", name=nombre)


@app.route("/mensaje")
def mensaje():
    return render_template("mensaje.html")



if __name__ == "__main__":
    app.run(debug=True)
