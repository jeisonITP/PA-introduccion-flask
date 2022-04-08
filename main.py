from flask import Flask, render_template, request, redirect, url_for, flash, session
from controllers import productosController

app = Flask(__name__)
app.secret_key = 'fjifjidfjied5df45df485h48@'

def estaIniciado():
    return True if 'usuario_id' in session else False

@app.get("/")
def index():
    if not estaIniciado():
        return redirect(url_for('loginForm'))
    
    productos = productosController.listarProductos()
    
    return render_template("index.html", productos=productos)

@app.get("/crear")
def crearProducto():
    if not estaIniciado():
        return redirect(url_for('loginForm'))
    return render_template("crear.html")

@app.post("/crear")
def crearProductoPost():
    if not estaIniciado():
        return redirect(url_for('loginForm'))
    
    nombre = request.form.get('nombre')
    
    imagen = request.files['imagen']
    
    price = request.form.get('price')
    
    if not productosController.crearProductoController(nombre, price, imagen):
        return render_template("crear.html", nombre = nombre, price = price)
    
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
    
@app.get("/login")
def loginForm():
    return render_template('login.html')

@app.post("/login")
def loginPost():
    
    #validacion de usuario y contraseña
    
    
    #Creacion de la sesion
    session['usuario_id'] = 5
    
    return "Iniciando"

@app.get("/cerrar_sesion")
def cerrarSesion():
    if not estaIniciado():
        return redirect(url_for('loginForm'))
    
    session.clear()
    
    return redirect(url_for('loginForm'))

#/edad/27 Tu naciste en el año 19

app.run(debug=True)
