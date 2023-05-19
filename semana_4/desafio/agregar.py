from inmuebles import listaInmuebles
from validarInmueble import *
from preguntaFinal import PreguntaFinal

#Agrega un nuevo inmueble y verifica uno por uno que los datos sean validos
def Agregar():
    print("Ingresar datos del inmueble.")

    anio = None
    metros = None
    habitaciones = None
    garage = None
    zona = None
    estado = None

    while True:
        anio = input("Año: ").strip()
        error, msg = ValidarAnio(anio)
        if error:
            print(msg)
        else:
            anio = int(anio)
            print("\n")
            break
        
    while True:
        metros = input("Metros: ").strip()
        error, msg = ValidarMetros(metros)
        if error:
            print(msg)
        else:
            metros = int(metros)
            print("\n")
            break
        
    while True:
        habitaciones = input("Habitaciones: ")
        error, msg = ValidarHabitaciones(habitaciones)
        if error:
            print(msg)
        else:
            habitaciones = int(habitaciones)
            print("\n")
            break
        
    print("Posee garage?\n1: SI.\n2: NO.")
    opcionesGarage = {"1": True, "2": False}
    while True:
        opcionGarage = input("Ingrese el numero con la opcion: ").strip()
        if not opcionGarage in opcionesGarage.keys():
            print("ERROR: La opcion no es valida.")
        else:
            garage = opcionesGarage[opcionGarage]
            print("\n")
            break
        
    while True:
        opcion = input("Elegir zona:\n1: A.\n2: B.\n3: C.\n\nOpcion: ").strip()
        error, msg = ValidarZonas(opcion)
        if error:
            print(msg)
        else:
            zona = msg
            print("\n")
            break
        
    print("Elegir estado del inmueble.\n1: Disponible.\n2: Reservado.\n3: vendido.")
    while True:
        opcion = input("Estado: ").strip()
        error, msg = ValidarEstado(opcion)
        if error:
            print(msg)
        else:
            estado = msg
            print("\n")
            break
        
    AgregarALista(anio, metros, habitaciones, garage, zona, estado)
    print("Inmbueble agregado.")
    
    return PreguntaFinal()

def AgregarALista(anio=0, metros=0, habitaciones=0, garaje=False, zona="A", estado="Disponible"):
    nuevoInmueble = {
        "año": anio,
        "metros": metros,
        "habitaciones": habitaciones,
        "garaje": garaje,
        "zona": zona,
        "estado": estado
    }

    listaInmuebles.append(nuevoInmueble)