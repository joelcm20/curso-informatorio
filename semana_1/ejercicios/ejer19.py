""" 19-Escribe un programa que solicite al usuario un número decimal y luego
imprima la parte entera y decimal por separado. """

decimal = input("Numero con decimales separados por \".\": ")
entero, decimales = decimal.split(".")
print(f"La parte entera es ({entero}) y los decimales son ({decimales})")