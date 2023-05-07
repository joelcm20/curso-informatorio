""" Escribe un programa que solicite al usuario su información personal, incluyendo
su nombre completo, edad, estatura, peso, dirección y número de teléfono.
A continuación, el programa deberá imprimir un mensaje con los datos
ingresados por el usuario en el siguiente formato:

La información ingresada es la siguiente:
Nombre completo: [nombre completo]
Edad: [edad]
Estatura: [estatura] cm
Peso: [peso] kg
Dirección: [dirección]
Número de teléfono: [número de teléfono] """

nombreCompleto = input("Nombre completo: ")
edad = input("Edad: ")
estatura = input("Estatura: ")
peso = input("Peso: ")
direccion = input("Direccion: ")
telefono = input("Telefono: ")

print(f"""
Nombre completo: {nombreCompleto}
Edad: {edad}
Estatura: {estatura} cm
Peso: {peso} kg
Dirección: {direccion}
Número de teléfono: {telefono}
""")