""" 13-Crear una lista con los nombres de tres colores y agregar dos colores más al
final de la lista. Mostrar la lista resultante. """

listaColores = ["verde", "rojo", "azul"]
listaColores.insert(len(listaColores),"negro")
listaColores.insert(len(listaColores),"blanco")
print(listaColores)