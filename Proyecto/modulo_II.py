from main import *
def compra_de_Entrada():
    name = input("Ingrese su nombre: ")
    id = input("Ingrese su C.I: ")
    edad = input("Ingrese su edad: ")
    
    for partido in lista_partidos:
        partido.mostrar()
    
    numero_de_partidos = input("Ingrese el numero de partido que desea ver: ")
    tipo_de_entrada =input("Ingrese g si quiere GENERAL o v si quiere VIP: ")
    if tipo_de_entrada == "g":
        precio = 35
    if tipo_de_entrada == "v":
        precio = 75 



