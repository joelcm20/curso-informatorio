from agregarEditarEliminar import AgregarEditarEliminar
from cambiarEstadoInmueble import CambiarEstadoInmueble
from busquedaInmueble import BusquedaInmueble
from listarInmuebles import ListarInmuebles

# menu: retorna la funcion segun la opcion elegida
casos = {
    "1": AgregarEditarEliminar,
    "2": CambiarEstadoInmueble,
    "3": BusquedaInmueble,
    "4": ListarInmuebles
}