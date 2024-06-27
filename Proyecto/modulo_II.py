from main import *
from Cliente import *
from entrada import *

lista_clientes = []
lista_entradas = []

def compra_de_Entrada(lista_partidos):
    name = input("Ingrese su nombre: ")
    id = input("Ingrese su C.I: ")
    edad = input("Ingrese su edad: ")
    
    for partido in lista_partidos:
        partido.mostrar()
    
    numero_de_partidos = input("Ingrese el numero de partido que desea ver: ")
    for partido in lista_partidos:
        if partido.number == numero_de_partidos:
            part = partido
            break
    part.venta += 1
    tipo_de_entrada =input("Ingrese g si quiere GENERAL o v si quiere VIP: ")
    if tipo_de_entrada == "g":
        tipo_de_entrada = "GENERAL"
        precio = 35

    if tipo_de_entrada == "v":
        tipo_de_entrada = "VIP"
        precio = 75

    if num_vampiro(id):
        descuento = 0.5 * precio

    else:
        descuento = 0
    iva = precio * 0.16
    total = precio - descuento + iva

    
    nuevoCliente = Cliente (name, id, edad, tipo_de_entrada)
    lista_clientes.append(nuevoCliente)
    
    nuevaentrada = Entrada (part, nuevoCliente)
    nuevoCliente.entradas.append(nuevaentrada)
    nuevoCliente.gastos += total
    print(f"""
    name = {name}
    edad = {edad}
    tipo_de_entrada = {tipo_de_entrada} 
    precio = {precio}
    iva = {iva} 
    descuento = {descuento}
    total = {total}

""")

def num_vampiro(cedula):
    if len(str(cedula)) %2 != 0:
        return False
    divisores = []
    for i in range(1, cedula):
        if cedula % i == 0:
            divisores.append(i)
    
    print (divisores)
    aux = []
    for divisor in divisores:
        if len(str(divisor)) != len(str(cedula)) /2:
            aux.append(divisor)
    for a in aux:
        divisores.remove(a)
    aux2 = []
    for divisor in divisores:
        guardar = True
        for i in str(divisor):
            if i not in str(cedula):
                guardar = False
        if not guardar:
            aux2.append(divisor)
    for a in aux2:
        divisores.remove(a)
    
    print (divisores)
    for x in range(len(divisores)-1):
        for y in range(x, len(divisores)):
            if divisores[x] * divisores[y] == cedula:
                return True
    return False





