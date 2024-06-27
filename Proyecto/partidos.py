class Partidos: 
    def __init__(self, id, number, home, away, date, group, stadium):
        self.id = id 
        self.number = number 
        self.home = home 
        self.away = away 
        self.date = date 
        self.group = group 
        self.stadium = stadium
        self.venta = 0
        self.asistencia = 0
    
    def mostrar(self):
        print(f"""
        id = {self.id}
        Number = {self.number}
        home = {self.home}
        away = {self.away}
        date = {self.date}
        group = {self.group}
        stadium = {self.stadium}

""")
