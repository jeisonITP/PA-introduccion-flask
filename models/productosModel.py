from config.database import db

def obtenerProductos():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute('select * from productos')
    
    productos = cursor.fetchall()
    #producto = cursor.fetchone()
    cursor.close()
    
    return productos

def crearProducto(nombre, price, imagen):
    cursor = db.cursor()
    
    cursor.execute("insert into productos(nombre, price, imagen) values(%s,%s,%s)", (
        nombre,
        price,
        imagen,
    ))
    
    cursor.close()