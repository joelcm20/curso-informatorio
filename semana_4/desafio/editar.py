from inmuebles import listaInmuebles as LM
from validarInmueble import *
from preguntaFinal import PreguntaFinal

def Editar():
    print("Elige de la lista de inmuebles cual desea editar.\n")
    
    print("- [Lista de inmuebles]")
    for i in range(0, len(LM)):
        numero = i+1
        anio = LM[i]["año"]
        metros = LM[i]["metros"]
        habitaciones = LM[i]["habitaciones"]
        garaje = LM[i]["garaje"]
        zona = LM[i]["zona"]
        estado = LM[i]["estado"]
        print(f"[{numero}] Año: {anio}, Metros: {metros}, habitaciones: {habitaciones}, Garaje: {garaje}, Zona: {zona}, Estado: {estado}")
    
    cantidadInmuebles = len(LM)
    
    while True:
        indice = input("\nIngresa el numero dentro de corchetes: ").strip()
        if not indice.isdigit() or not int(indice) >= 1 and int(indice) < cantidadInmuebles:
            print(f"El numero debe ser un digito valido entre el 1 y el {cantidadInmuebles}")
        else: break
    
    indice = int(indice)-1
    print("Ingresa los nuebos datos.\n")
    for key in LM[indice].keys():
        if key == "garaje":
            print(f"Posee garage? (valor actual: {LM[indice][key]})\n1: SI.\n2: NO.\n3: Valor Actual.")
            opcionesGarage = {"1": True, "2": False, "3": LM[indice][key]}
            while True:
                opcionGarage = input("Ingrese el numero con la opcion: ").strip()
                if not opcionGarage in opcionesGarage.keys():
                    print("ERROR: La opcion no es valida.")
                else:
                    garage = opcionesGarage[opcionGarage]
                    print("\n")
                    break
            LM[indice][key] = garage
        elif key == "zona":
            print(f"Elegir zona (valor actual {LM[indice][key]})\n1: A.\n2: B.\n3: C.\n4: Valor Actual.")
            while True:
                opcion = input("Opcion: ").strip()
                if opcion == "4":
                    break
                else:
                    error, msg = ValidarZonas(opcion)
                    if error:
                        print(msg)
                    else:
                        zona = msg
                        print("\n")
                        break
            LM[indice][key] = zona
        elif key == "estado":
            print(f"Elegir estado del inmueble (valor actual {LM[indice][key]})\n1: Disponible.\n2: Reservado.\n3: vendido.\n4: Valor actual")
            while True:
                opcion = input("Estado: ").strip()
                if opcion == "4":
                    break
                else:
                    error, msg = ValidarEstado(opcion)
                    if error:
                        print(msg)
                    else:
                        estado = msg
                        print("\n")
                        break
            LM[indice][key] = estado
        else:
            if key == "año":
                while True:
                    anio = input(f"{key.capitalize()} (valor actual: {LM[indice][key]}) | dejar vacio para el valor actual: ").strip()
                    if not anio == "":
                        error, msg = ValidarAnio(anio)
                        if error:
                            print(msg)
                        else:
                            break
                    else:
                        anio = LM[indice][key]
                        break
                LM[indice][key] = int(anio)
            elif key == "metros":
                while True:
                    metros = input(f"{key.capitalize()} (valor actual: {LM[indice][key]}) | dejar vacio para el valor actual: ").strip()
                    if not metros == "":
                        error, msg = ValidarMetros(metros)
                        if error:
                            print(msg)
                        else:
                            break
                    else:
                        metros = LM[indice][key]
                        break
                LM[indice][key] = int(metros)
            else:
                while True:
                    habitaciones = input(f"{key.capitalize()} (valor actual: {LM[indice][key]}) | dejar vacio para el valor actual: ").strip()
                    if not habitaciones == "":
                        error, msg = ValidarHabitaciones(habitaciones)
                        if error:
                            print(msg)
                        else:
                            break
                    else:
                        habitaciones = LM[indice][key]
                        break
                LM[indice][key] = int(habitaciones)
    return PreguntaFinal()