""" 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
dd/mm/aaaa y luego imprima su edad en años.
Utiliza la función .split() """

nacimiento = input("fecha de nacimiento con formato dd/mm/aa: ")
anio = nacimiento.split("/")[2]
edad = 2023 - int(anio)
print(f"Tu edad es: {edad}")