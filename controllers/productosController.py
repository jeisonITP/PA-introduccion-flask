from flask import flash
from models import productosModel

def listarProductos():
    return productosModel.obtenerProductos()

def crearProductoController(nombre, price, imagen):
    try:
        price = int(price)
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
        return False
    
    
    imagen.save('./static/image/' + imagen.filename)
    
    productosModel.crearProducto(nombre=nombre, 
                                 price=price,
                                 imagen='/static/image/' + imagen.filename)
    
    return True