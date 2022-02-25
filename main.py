from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")

@app.get("/contacto/<int:contactoId>/edit")
def editarContacto(contactoId):
    suma = 2+2
    
    return render_template('contactos/editar.html', 
        contactoId = contactoId, 
        suma = suma
    )

#/edad/27 Tu naciste en el año 19

app.run(debug=True)
