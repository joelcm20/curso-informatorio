""" 14-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5 """

numero = int(input("Ingresar un numero: "))
piramide = ""

i = 1
while i <= numero:
    preparar_fila = f"{i}"
    fila = preparar_fila*i
    piramide += fila+"\n"
    i += 1

print(piramide)
