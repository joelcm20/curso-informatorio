# opcion para volver al menu
def PreguntaFinal():
    print("\n¿Deseas seguir en el programa?:\nSI: ingresa 1.\nNO: ingresa cualquier letra")
    respuesta = input("Opcion: ").strip()
    return respuesta == "1"