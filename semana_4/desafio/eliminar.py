from inmuebles import listaInmuebles as LM
from preguntaFinal import PreguntaFinal

# Eliminar inmueble de la lista segun el indice ingresado
def Eliminar():
    print("Elige de la lista de inmuebles cual desea eliminar.\n")
    
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

    del LM[int(indice)-1]
    print("El inmueble ha sido eliminado correctamente.")
    return PreguntaFinal()