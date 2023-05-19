from inmuebles import listaInmuebles as LM
from validarInmueble import ValidarEstado
from preguntaFinal import PreguntaFinal

# modifica el estado del inmueble elegido de la lista mostrada
def CambiarEstadoInmueble():
    print("Elige de la lista de inmuebles cual desea cambiar el estado.\n")
    
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
    
    print("""
    Elige de las opciones que estado poner.
    1: Disponible.
    2: Reservado.
    3: Vendido.
    """)

    while True:
        opcion = input("Opcion: ").strip()
        error, msg = ValidarEstado(opcion)
        if error:
            print(msg)
        else:
            break

    LM[int(indice)-1]["estado"] = msg
    print("El estado del inmueble ha sido cambiado correctamente.")
    return PreguntaFinal()