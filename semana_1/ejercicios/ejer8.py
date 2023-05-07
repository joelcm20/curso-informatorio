""" 8-Crea un programa que pida al usuario el radio de un círculo y muestre su
diámetro, su circunferencia y su área.
Supón que pi es aproximadamente 3.14159. """

PI = 3.14159

print("Calculando diametro, circunferencia y area de un circulo a partir de su radio")
radio = int(input("Radio: "))
diametro = int(radio*2)
circunsferencia = 2 * PI * radio
area = PI * radio ** 2
print(f"El diametro es de: {diametro}")
print(f"La circunsferencia es de: {circunsferencia}")
print(f"El area es de: {area}")
