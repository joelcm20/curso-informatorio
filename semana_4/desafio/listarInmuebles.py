from inmuebles import listaInmuebles as LM
from preguntaFinal import PreguntaFinal

# listar todos los inmuebles
def ListarInmuebles():
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
    
    return PreguntaFinal()
    