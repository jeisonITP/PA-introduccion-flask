# Este es un comentario de una sola linea

'''
Este es un comentario de multiple linea
con comilla sencilla
'''
"""
Este es un comentario de multiple linea
con comilla doble
"""

#Variables
nombrePersona = "" #String
edad = 27 # int
numeroDecimal = 10.2 # float
esMayorEdad = True # False Boolean

#Debug
print(nombrePersona) # Jeyson

# Array Arreglo Listas []

diasSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves']

print(diasSemana[2]) # Miercoles

arrayMultiple = [1, 'hola', [5,6,[7,8]]]

print(arrayMultiple[2][2][1]) # 8

# Objectos JSON Diccionarios {}

persona = {
    'nombre': 'Jeyson',
    'apellido': 'Calvache',
    'edad': 27,
    'lenguajes': ['Python', 'Javascript'],
    'prueba': 'Prueba'
}

nombrePersona = persona['prueba']

print(persona)
print(persona['nombre']) # Jeyson
print(persona['lenguajes'][1]) # Javascript

#Listas de diccionarios
personas = [
    {
        'nombre': 'Jeyson',
        'apellido': 'Calvache',
        'edad': 27,
        'lenguajes': ['Python', 'Javascript'],
        'prueba': 'Prueba'
    },
    {
        'nombre': 'Juan',
        'apellido': 'Perez',
        'edad': 27,
        'lenguajes': ['Java', '.Net'],
        'prueba': 'Prueba'
    },
    {
        'nombre': 'Pepito',
        'apellido': 'Perez',
        'edad': 27,
        'lenguajes': ['Go', 'Rust'],
        'prueba': 'Prueba'
    }
]

print(persona[1]['lenguajes'][1])


#Condiciones

if esMayorEdad == True:
    print('Es mayor de edad')
else:
    print('No es mayor de edad')

print('Terminado')

