""" Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
sus ventas totales y el departamento comercial te solicita que ayudes a los
vendedores a calcular sus comisiones creando un programa que les pregunte su
nombre y cuánto han vendido en éste mes.
Tu programa le va a responder con una frase que incluya su nombre y el monto
que le corresponde por las comisiones """

print("Calculadora de comisiones...")
nombre = input("Nombre: ")
ventasTotales = float(input("Ventas totales del mes: "))
corresponde = ventasTotales * 0.06

print(f"{nombre}, el monto que te corresponde por las comisiones es de: {corresponde}")