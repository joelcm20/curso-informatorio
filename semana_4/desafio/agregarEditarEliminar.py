from casosAgregarEditarEliminar import casosAgregarEditarEliminar

def AgregarEditarEliminar():
    print("""
    Elige la operacion:
    1: Agregar.
    2: Editar.
    3: Eliminar.
    """)

    operacionesDisponibles = ["1", "2", "3"]
    
    while True:
        operacion = input("Operacion: ").strip()
        if not operacion in operacionesDisponibles:
            print("ERROR: La opcion no es valida.")
        else: break
    
    return casosAgregarEditarEliminar[operacion]()

    
    
    

    
