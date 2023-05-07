""" 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
e imprima su índice de masa corporal (IMC).
La fórmula para calcular el IMC es: IMC = peso / (altura ** 2). """

print("Vamos a calcular tu IMC(índice de masa corporal)...")
peso = float(input("peso: "))
altura = float(input("altura: "))
print(f"Tu IMC es: {peso/(altura**2)}")