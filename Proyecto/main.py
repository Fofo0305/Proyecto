import requests
from equipo import *
from producto import *
from restaurants import *
from estadio import *
from partidos import *
equipos= requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()
estadios = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json").json()
partidos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json").json()
lista_equipos = []
lista_estadios = []
lista_partidos = []
def crearObjetos():

    """equipos = [
  {
    "id": "31c88261-1efd-444e-95ac-b7c1cd034bfd",
    "code": "GER",
    "name": "Germany",
    "group": "A"
  }
  ]"""
    for equipo in equipos:
        nuevoEquipo = Equipo(equipo["id"], equipo["code"], equipo["name"], equipo["group"])
        lista_equipos.append(nuevoEquipo)

    """estadios =[ 
  {
    "id": "2eead114-7627-45c4-83ab-ee3d66a6c62f",
    "name": "Estadio Olímpico de Berlín",
    "city": "Berlín",
    "capacity": [
      133,
      319
    ],
    "restaurants": [
      {
        "name": "Centeno S.L.",
        "products": [
          {
            "name": "Increible Plástico Teclado",
            "quantity": 3820,
            "price": "868.00",
            "stock": 355,
            "adicional": "plate"
          }
        ]
    }
    ]
}
]"""

    for stadium in estadios:  
        l_rest = []
        for tipo, dato in stadium.items(): 
            if tipo == "restaurants":
                for restaurant in dato:
                    l_productos = []
                    for i, d in restaurant.items():
                        if i == "products": 
                            for products in d:
                                nuevoProducto = Producto(products["name"], products["quantity"], products["price"], products["stock"], products["adicional"]) 
                                l_productos.append()
                        nuevoRestaurante = Restaurants(restaurant["name"],l_productos)
                        l_rest.append(nuevoRestaurante)
        nuevoEstadio = Estadio(estadios[id], estadios["name"], estadios["city"], estadios["capacity"],l_rest)         
        """
        partidos = [  {
            "id": "1304daa3-c591-464e-adbc-192538de2e40",
            "number": 1,
            "home": {
            "id": "31c88261-1efd-444e-95ac-b7c1cd034bfd",
            "code": "GER",
            "name": "Germany",
            "group": "A"
            },
            "away": {
            "id": "d18b547a-3e55-4ead-a73a-6ee9af05c761",
            "code": "SCO",
            "name": "Scotland",
            "group": "A"
            },
            "date": "2024-06-14",
            "group": "Group A",
            "stadium_id": "3db1375b-a28f-4908-9878-ec0fe5a5587f"
        }
        ]"""

    for partidos in partidos:
        for tipo, dato in partidos.items(): 
            home = ""
            away = ""
            estadio = ""
            if tipo == "home":
                for equipo in lista_equipos:
                    if equipo.id == dato["id"]:
                        home = equipo
            if tipo == "away":
                for equipo in lista_equipos:
                    if equipo.id == dato["id"]:
                        away = equipo 
            if tipo == "estadio":
                for equipo in lista_estadios:
                    if equipo.id == dato["id"]:
                        estadio = equipo
        nuevoPartidos = Partidos(partidos ["id"], partidos["number"], home, away, partidos["date"], partidos["group"],estadio)

def buscarPais(lista_partidos):
    pais = input("Ingrese el codigo del pais: ")
    lista = []
    for partido in lista_partidos:
        if partido.home.code == pais or partido.away.code == pais:
            lista.append(partido)
    
    for partido in lista:
        partido.mostrar()

def BuscarEstadio(lista_partidos):
    estadio = input("ingrese el nombre del estadio: ")
    lista = []
    for partido in lista_partidos:
        if partido.estadio.name == estadio: 
            lista.append(partido)

    for partido in lista:
        partido.mostrar()

def buscarFecha(lista_partidos):
    date = input("ingrese la fecha del partido: ")
    lista = []
    for partido in lista_partidos:
        if partido.date == date:
            lista.append(partido)

    for partido in lista:
        partido.mostrar()
