from d4_g11 import *


def mostrar_menu():
    print("Bienvenido a la aplicación de gestión de inmuebles.")
    print("1. Agregar inmueble")
    print("2. Editar inmueble")
    print("3. Eliminar inmueble")
    print("4. Cambiar estado de inmueble")
    print("5. Buscar inmuebles por presupuesto")
    print("6. Ver lista de inmuebles")
    print("0. Salir")


def agregar_inmueble_interfaz():
    inmueble = {}
    print("Ingrese los detalles del inmueble:")
    inmueble['año'] = int(input("Año: "))
    inmueble['metros'] = int(input("Metros: "))
    inmueble['habitaciones'] = int(input("Habitaciones: "))
    inmueble['garaje'] = bool(input("Garaje (True/False): "))
    inmueble['zona'] = input("Zona (A/B/C): ")
    inmueble['estado'] = input("Estado (Disponible/Reservado/Vendido): ")

    agregar_inmueble(lista_inmuebles, inmueble)


def editar_inmueble_interfaz():
    indice = int(input("Ingrese el índice del inmueble a editar: "))
    nuevo_inmueble = {}
    print("Ingrese los nuevos detalles del inmueble:")
    nuevo_inmueble['año'] = int(input("Año: "))
    nuevo_inmueble['metros'] = int(input("Metros: "))
    nuevo_inmueble['habitaciones'] = int(input("Habitaciones: "))
    nuevo_inmueble['garaje'] = bool(input("Garaje (True/False): "))
    nuevo_inmueble['zona'] = input("Zona (A/B/C): ")
    nuevo_inmueble['estado'] = input("Estado (Disponible/Reservado/Vendido): ")

    editar_inmueble(lista_inmuebles, indice, nuevo_inmueble)


def eliminar_inmueble_interfaz():
    indice = int(input("Ingrese el índice del inmueble a eliminar: "))
    eliminar_inmueble(lista_inmuebles, indice)


def cambiar_estado_interfaz():
    indice = int(input("Ingrese el índice del inmueble: "))
    nuevo_estado = input(
        "Ingrese el nuevo estado (Disponible/Reservado/Vendido): ")
    cambiar_estado(lista_inmuebles, indice, nuevo_estado)


def buscar_inmuebles_interfaz():
    presupuesto = float(input("Ingrese el presupuesto máximo: "))
    resultados = buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto)

    if resultados:
        print("Inmuebles encontrados:")
        for inmueble in resultados:
            print(inmueble)
    else:
        print("No se encontraron inmuebles dentro del presupuesto.")


def mostrar_lista_inmuebles():
    if lista_inmuebles:
        print("Lista de inmuebles:")
        for indice, inmueble in enumerate(lista_inmuebles):
            print(f"Inmueble {indice}:")
            print(inmueble)
    else:
        print("No hay inmuebles en la lista.")


# Programa principal
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_inmueble_interfaz()
    elif opcion == "2":
        editar_inmueble_interfaz()
    elif opcion == "3":
        eliminar_inmueble_interfaz()
    elif opcion == "4":
        cambiar_estado_interfaz()
    elif opcion == "5":
        buscar_inmuebles_interfaz()
    elif opcion == "6":
        mostrar_lista_inmuebles()
    elif opcion == "0":
        print("Gracias por usar la aplicación. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")


print(lista_inmuebles)
