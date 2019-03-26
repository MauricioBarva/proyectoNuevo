from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('tareas.html')

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

    
app.run(debug=True)