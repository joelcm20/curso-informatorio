""" 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
los números naturales del 1 hasta ese número. """

numero = int(input("Ingresar numero: "))
i = 1
suma = 0
while i <= numero:
    suma += i
    i += 1
print(f"La suma del 1 hasta {numero} es: {suma}")
