from flask import Flask, render_template, request, redirect, url_for, flash
from models import productosModel

app = Flask(__name__)
app.secret_key = 'fjifjidfjied5df45df485h48@'

@app.get("/")
def index():
    productos = productosModel.obtenerProductos()
    
    return render_template("index.html", productos=productos)

@app.get("/crear")
def crearProducto():
    return render_template("crear.html")

@app.post("/crear")
def crearProductoPost():
    nombre = request.form.get('nombre')
    
    try:
        price = int(request.form.get('price'))
    except:
        price = 0
        
    isValid = True
    
    if nombre == "":
        isValid = False
        flash("el nombre es obligatorio")

    if price == "":
        isValid = False
        flash("el precio es obligatorio")

    if price <= 0:
        isValid = False
        flash("el precio debe ser mayor a cero")
    
    if isValid == False:
        return render_template("crear.html", nombre = nombre, price = price)
    
    productosModel.crearProducto(nombre=nombre, price=price)
    
    return redirect(url_for('index'))

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
