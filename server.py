from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import logging

import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_tarea = db.Column(db.String(100), nullable = False)
    nombre_materia = db.Column(db.String(100), nullable = False)
    fecha_tarea = db.Column(db.String(100), nullable = False)
    descripcion_tarea = db.Column(db.String(250), nullable = False)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            new_tarea = Tareas(nombre_tarea = request.form["nombre"], nombre_materia = request.form["materia"], fecha_tarea = request.form["fecha"], descripcion_tarea = request.form["descripcion"])
            db.session.add(new_tarea)
            db.session.commit()
        except Exception as e:
            
            return app.logger.error("El error fue: "+ str(e))

    return render_template('tareas.html')

@app.route('/tareas')
def tareas(): 
    return render_template('historial.html', Tareas = Tareas.query.all())

db.create_all()
app.run(debug=True)