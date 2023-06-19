from datetime import datetime, timedelta

class Pizza:
    def __init__(self, code, name, ingredients, price, size, type):
        self.code = code
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.size = size
        self.type = type


class Client:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def make_order(self, code_pizza, quantity):
        return Order(self, code_pizza, quantity)


class Order:
    def __init__(self, client, code_pizza, quantity):
        self.client = client
        self.code_pizza = code_pizza
        self.quantity = quantity
        self.date = datetime.now()
        self.delivery_time = self.date+timedelta(minutes=30)


class Pizzeria:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.variants = []
        self.orders = []

    def add_variant(self, code, name, ingredients, price, size, type):
        self.variants.append([Pizza(code, name, ingredients, price, size, type), 0])

    def show_menu(self):
        for v in self.variants:
            print(f"code nº {v[0].code}: {v[0].name} {v[0].size} a la {v[0].type} de ${v[0].price}, ingrediente: {v[0].ingredients}")
    
    def take_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("El tipo de pedido no es correcto")
        else:
            for v in self.variants:
                if v[0].code == order.code_pizza:
                    self.orders.append([order, False])
                    v[1] += order.quantity
                    return
            raise ValueError("La pizza no existe")
    
    def get_pupular_pizza(self):
        pizza = self.variants[0]
        for v in self.variants:
            if v[1] > pizza[1]:
                pizza = v
        return pizza[0]
    
    def income(self, _from, _to=datetime.now()):
        income = 0

    
    def finish_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("El tipo de pedido no es correcto")
        else:
            try:
                self.orders.remove(order)
            except ValueError:
                print("La orden no existe")
            


pizzeria = Pizzeria("Luigui", "Calle 1", "123456789", "fJ7iV@example.com")
pizzeria.add_variant(1, "Margarita", "Margarita", 10, "grande", "molde")
pizzeria.add_variant(2, "Comun", "Jamon y Queso", 10, "mediana", "parrilla")
pizzeria.show_menu()

messi = Client("Lionel", "Messi")
neymar = Client("Neymar", "jr")

order1 = messi.make_order(2, 2)
order2 = neymar.make_order(1, 3)
pizzeria.take_order(order1)
pizzeria.take_order(order2)

pizzeria.finish_order(order1)
pizzeria.finish_order(order2)

print("pizza popular")
print(pizzeria.get_pupular_pizza().name)

print("Ingresos")
print(pizzeria.income())