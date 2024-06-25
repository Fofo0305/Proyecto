class Producto:
    def __init__(self, name, quantity, price, stock, adicional, clasificacion):
        self.name = name 
        self.quantity = quantity
        self.price = price 
        self.stock = stock 
        self.adicional= adicional
        self.clasificacion = clasificacion

    def mostrar(self):
        print(f"""
        name = {self.name}
        quantity = {self.quantity}
        price = {self.price}
        stock = {self.stock}
        adicional = {self.adicional}
        clasificacion = {self.clasificacion}
""")