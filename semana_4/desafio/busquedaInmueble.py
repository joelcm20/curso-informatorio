from inmuebles import listaInmuebles as lista
from preguntaFinal import PreguntaFinal

# pide presupuesto y devuelve una lista con los inmuebles disponibles segun el presupuesto
def BusquedaInmueble():
    presupuesto = input("Ingresa un presupuesto para hacer el filtrado: ")

    inmuebles_encontrados = []
    for inmueble in lista:
        precio = calcular_precio(inmueble)
        if inmueble['estado'] in ['Disponible', 'Reservado'] and int(precio) <= int(presupuesto):
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio
            inmuebles_encontrados.append(inmueble_con_precio)
    
    if len(inmuebles_encontrados) < 1:
        print("Sin resultado!")
    else:
        for i in range(0, len(inmuebles_encontrados)):
            numero = i+1
            anio = inmuebles_encontrados[i]["año"]
            metros = inmuebles_encontrados[i]["metros"]
            habitaciones = inmuebles_encontrados[i]["habitaciones"]
            garaje = inmuebles_encontrados[i]["garaje"]
            zona = inmuebles_encontrados[i]["zona"]
            estado = inmuebles_encontrados[i]["estado"]
            precio = inmuebles_encontrados[i]["precio"]
            print(f"[{numero}] Año: {anio}, Metros: {metros}, habitaciones: {habitaciones}, Garaje: {garaje}, Zona: {zona}, Estado: {estado}, Precio {precio}")
    
    return PreguntaFinal()



#  calcular_precio recibe un diccionario que representa un inmueble y calcula su precio basado en las reglas establecidas en las consignas..
def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['año']
    zona = inmueble['zona']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = int(inmueble['garaje'])

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    else:
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2

    return precio