class Restaurants:
    def __init__(self,name, products):
        self.name = name 
        self.products = products

    def mostrar(self):
        print(f"""
       name = {self.name}
        products = {self.products}
""")