""" 12-Escribe un programa que pida al usuario una lista de números separados por
comas y calcule su promedio. """

numeros = input("Ingresar 2 o mas numeros separados por \",\": ").split(",")
numeros_suma_total = 0
promedio = 0

for numero in numeros:
    numeros_suma_total += int(numero)

promedio = numeros_suma_total / len(numeros)
print(f"El promedio de los numeros ingresados es: {promedio}")