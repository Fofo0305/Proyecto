class Cliente: 
    def __init__(self,name,id,edad,tipo_de_entrada):
        self.name = name 
        self.id = id
        self.edad = edad 
        self.tipo_de_entrada = tipo_de_entrada
        self.entradas = []

    def mostrar(self):
        print(f"""
        name = {self.name}
        id = {self.id}
        edad = {self.edad}
        tipo_de_entrada = {self.tipo_de_entrada}
""")

