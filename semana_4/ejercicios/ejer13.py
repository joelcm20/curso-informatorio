""" 13-Crea una función llamada calcular_descuento que tome dos parámetros:
precio y porcentaje_descuento. La función debe calcular y devolver el precio
después de aplicar el descuento. """


def calcular_descuento(precio, porcentaje_descuento):
    return precio - precio * float(f"0.{porcentaje_descuento}")

print(calcular_descuento(200, 10))
