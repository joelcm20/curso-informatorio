""" 13-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de asteriscos con esa cantidad de filas. """

numero = int(input("Ingresar un numero: "))
piramide = ""

i = 1
while i <= numero:
    piramide += "*"*i+"\n"
    i += 1

print(piramide)
