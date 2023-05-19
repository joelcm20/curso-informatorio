from agregar import Agregar
from editar import Editar
from eliminar import Eliminar

# retorna la funcion segun la opcion elegida
casosAgregarEditarEliminar = {
    "1": Agregar,
    "2": Editar,
    "3": Eliminar,
}