""" GRUPO 11
Desafío 4: La inmobiliaria
"""
# Requisitos técnicos: Operadores, Estructuras de datos, Estructuras de control de flujo y Funciones


# Una inmobiliaria de tu ciudad solicita un sistema para automatizar la gestión de sus inmuebles.
# Se te pide construir un programa que permita:
#  Agregar, editar y eliminar inmuebles a la lista.
# Las funciones deben ajustarse al formato de lista y reglas de validación.
#  Cambiar el estado de un inmueble, sin modificar sus demás datos.
# Las funciones deben ajustarse al formato de lista y reglas de validación.
#  Hacer búsqueda de inmuebles en función de un presupuesto dado.


# Recibe una lista de inmuebles y un diccionario que representa un nuevo inmueble
# Si la validacion nos da True, se agrega con .append a la lista.
def agregar_inmueble(lista, inmueble):
    if validar_inmueble(inmueble):
        lista.append(inmueble)
        print("El inmueble ha sido agregado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")


#  recibe una lista de inmuebles, un índice que indica el inmueble a editar y un diccionario que representa el nuevo inmueble.
def editar_inmueble(lista, indice, nuevo_inmueble):
    if validar_inmueble(nuevo_inmueble):
        lista[indice] = nuevo_inmueble
        print("El inmueble ha sido editado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")


# recibe una lista de inmuebles y un índice que indica el inmueble a eliminar.
def eliminar_inmueble(lista, indice):
    del lista[indice]
    print("El inmueble ha sido eliminado correctamente.")


#  cambiar_estado recibe una lista de inmuebles, un índice que indica el inmueble a modificar y un nuevo estado...Si el nuevo estado no es válido, se muestra un mensaje de error.
def cambiar_estado(lista, indice, nuevo_estado):
    if nuevo_estado in ['Disponible', 'Reservado', 'Vendido']:
        lista[indice]['estado'] = nuevo_estado
        print("El estado del inmueble ha sido cambiado correctamente.")
    else:
        print("Estado inválido. los estados válidos son: Disponible, Reservado, Vendido.")


#  buscar_inmuebles_por_presupuesto recibe una lista de inmuebles y un presupuesto.
#  los inmuebles que cumplan con la condicione se agregan a una nueva lista junto con su precio, y finalmente se devuelve la lista de inmuebles encontrados.
def buscar_inmuebles_por_presupuesto(lista, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista:
        precio = calcular_precio(inmueble)
        if inmueble['estado'] in ['Disponible', 'Reservado'] and precio <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio
            inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados


# Aca esta funcion validar_inmueble realiza la validacion de cada inmueble, si la pasa a la validación, se agrega a la lista de inmuebles y se muestra un mensaje de éxito.
# Sino, se muestra un mensaje de error.
def validar_inmueble(inmueble):
    if inmueble['zona'] not in ['A', 'B', 'C']:
        return False
    if inmueble['estado'] not in ['Disponible', 'Reservado', 'Vendido']:
        return False
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60 or inmueble['habitaciones'] < 2:
        return False
    return True


#  calcular_precio recibe un diccionario que representa un inmueble y calcula su precio basado en las reglas establecidas en las consignas..
def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['año']
    zona = inmueble['zona']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = int(inmueble['garaje'])

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100) * 1.5
    else:
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100) * 2

    return precio


# Esta es la lista de los inmuebles, con uno ya puesto por default.
lista_inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4,
                    'garaje': True, 'zona': 'C', 'estado': 'Disponible'}]

print(lista_inmuebles)


# Integrantes Grupo 11:
# Renzo, Arrieta
# Pablo, Acevedo
# Matías Gastón, Serial Trachta
# Lugo Mauro, Rodrigo
# Julio R, Escanciano Gonzalez
# Facundo, Vicedo
# Gabriel, Leiva
# Joel, Chavez
# Maximiliano Imanol, Aguer
# Cristian J, Salto
