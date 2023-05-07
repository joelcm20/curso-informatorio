""" 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
multiplicar correspondiente a ese número del 1 al 10. """

numero = int(input("Ingresa un numero: "))
i = 1
while i <= 10:
    print(f"{numero}x{i}={numero*i}")
    i += 1
