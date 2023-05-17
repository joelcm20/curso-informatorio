from casos import casos

def index():
    while True:
        print("""
        [ Gestion de inmuebles ]

        ¿Que desea hacer?:
        1: Agregar, editar y eliminar inmuebles.
        2: Cambiar el estado de un inmueble.
        3: Hacer búsqueda de inmuebles en función de un presupuesto dado.
        4: Listar inmuebles.
        """)

        opcionesDisponibles = ["1", "2", "3", "4"]
        
        while True:
            opcion = input("Ingrese el numero que corresponda a la accion que desee hacer: ").strip()
            if not opcion in opcionesDisponibles:
                print("ERROR: La opcion no es valida.")
            else: break

        if not casos[opcion]() == True:
            print("Adios.")
            break
            


index()