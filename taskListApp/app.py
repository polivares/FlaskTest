from flask import Flask, render_template, request

app = Flask(__name__)
tareas = []
@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        tareas.append(request.form.get("tarea"))
    return render_template("index.html", tareas=tareas)


@app.route("/agregar.html")
def agregar():
    return render_template("agregar.html")
    # También existe el método redirect("/") para cambiar entre páginas


if __name__ == '__main__':
    app.run(debug=True)