from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))


@app.route('/')
def index():
    return render_template('tareas.html')

@app.route('/insert/default')
def insert_default():

    new_post = Posts(title="Default title")
    db.session.add(new_post)
    db.session.commit()

    return "the default was created"

@app.route('/lista/')
def historial():
    
    u1={'id': id, 'nombre': "Mauricio", 'puntos': 100}
    u2={'id': 31, 'nombre': "Sapo", 'puntos': 900}
    u3={'id': 8765, 'nombre': "Estiercol", 'puntos': 98765}

    l = []

    l.append(u1)
    l.append(u2)
    l.append(u3)
    return render_template('historial.html', lista = l)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)