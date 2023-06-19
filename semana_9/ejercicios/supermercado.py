class Producto:
    def __init__(self, name, price, staple_product, careful_price=False, discount=0.9):
        self.name = name
        self.price = price
        self.careful_price = careful_price
        self.staple_product = staple_product
        self.discount = discount
    
    def calculate_price(self):
        if self.staple_product:
            return self.price * self.discount
        else:
            return self.price

class Supermarket:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products = []
    
    def get_products_quantity(self):
        return len(self.products)
    
    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.calculate_price()
        return total_price
    
    def add_product(self, product):
        if not isinstance(product, Producto):
            raise TypeError("El producto no es un objeto de tipo Producto")
        self.products.append(product)


# super market
market = Supermarket("marcado-luis", "Av. Colinas 123")
# products
market.add_product(Producto("Pan", 150, True))
market.add_product(Producto("Leche", 200, True))
market.add_product(Producto("Gaseosa", 420, False))
market.add_product(Producto("Alfajor", 80, False))

def print_options():
    print("1. Mostrar el número de productos")
    print("2. Mostrar el precio total de los productos")
    print("3. Agregar un producto")
    print("0. Salir")

while True:
    print_options()
    try:
        option = int(input("Ingrese una opción: "))
    except ValueError:
        print("Opción no válida")
        continue
    if option == 0:
        break
    elif option == 1:
        print(f"El número de productos es: {market.get_products_quantity()}")
    elif option == 2:
        print(f"El precio total es: {market.get_total_price()}")
    elif option == 3:
        name = input("Ingrese el nombre del producto: ")
        price = int(input("Ingrese el precio del producto: "))
        staple_product = input("¿Es un producto basico? (si/no): ")
        careful_price = input("¿Es un producto con precio cuidado? (si/no): ")
        if staple_product == "si":
            product = Producto(name, price, True)
        else:
            product = Producto(name, price, False)
        if careful_price == "si":
            product.careful_price = True
        
        market.add_product(product)
    else:
        print("Opción no válida")
