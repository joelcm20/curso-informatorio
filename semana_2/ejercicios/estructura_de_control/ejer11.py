""" 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
la suma de ellos solo si ambos son pares. """

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print(f"La suma de ambos numeros es: {numero1+numero2}")
else:
    print("Uno o ambos numeros no son pares, no se puede hacer la suma")