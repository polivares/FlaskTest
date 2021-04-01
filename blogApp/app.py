from flask import Flask, render_template, request, redirect
from db import db, Post

app = Flask(__name__)
# BD configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Connect db with app var
db.init_app(app)
# Add context for app
with app.app_context():
    # db.drop_all() For droping tables
    db.create_all()  # For creating for model


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        id = request.form.get("post_id")
        post = db.session.query(Post).filter(Post.id == id).first()
        db.session.delete(post)
        db.session.commit()
    posts = Post.query.order_by(Post.fecha.desc()).all()
    return render_template("index.html", posts=posts)


@app.route("/agregar", methods=["GET","POST"])
def agregar():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        text = request.form.get("text")
        post = Post(titulo=titulo, text=text)
        # Adding data into de DB
        db.session.add(post)
        db.session.commit()

    return render_template("agregar.html")



if __name__ == '__main__':

    app.run(debug=True)
