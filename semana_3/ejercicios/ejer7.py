""" 7-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
izquierda). """

palabra = input("Ingresar palabra: ")
palabra_inverso = palabra[::-1]
if palabra == palabra_inverso:
    print(f"La palabra \"{palabra}\" es un palíndromo")
else:
    print(f"La palabra \"{palabra}\" no es palíndromo")