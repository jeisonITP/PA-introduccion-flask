from config.database import db

def obtenerProductos():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute('select * from productos')
    
    productos = cursor.fetchall()
    #producto = cursor.fetchone()
    cursor.close()
    
    return productos

def crearProducto(nombre, price):
    cursor = db.cursor()
    
    cursor.execute("insert into productos(nombre, price) values(%s,%s)", (
        nombre,
        price,
    ))
    
    cursor.close()