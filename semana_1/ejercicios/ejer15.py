""" 15-Escribe un programa que solicite al usuario una temperatura en grados
Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32. """

temperatura = int(input("Temperatura en grados celsius: "))
print(f"El equivalente de la temperatura {temperatura} en grados fahrenheit es {temperatura*1.8+32}")