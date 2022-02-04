# Muestra como crear mensajes de errores basados en determinadas acciones sobre una lista.
# Muy importante para q nuestro programa no se trabe o rompa.


lista = [5, 'casa', 0]

try:
    print(lista[3])
except IndexError:
    print('Fuera de rango. Escriba un rango dentro de la lista')
try:
    print(67 / lista[2])  
except ZeroDivisionError:
    print('No se puede dividir por cero. Escriba otro numero')
try:
    print(-12 + lista[1])
except TypeError:
    print('No se pueden sumar diferentes tipos de datos')     
try: 
    print(listado[1])
except NameError:
    print('Nombre no encontrado. Definirlo')

print('- Final del programa -') 