
from Cliente import*
from entrada import*
from validaciones import*
lista_clientes = []
lista_entradas = []

def compra_de_Entrada(lista_partidos):
    name = input("Ingrese su nombre: ")
    name = validar_string (name, "Ingrese su nombre: " )
    id = input("Ingrese su C.I: ")
    id = validar_int(id, "Ingrese su C.I: " )
    edad = input("Ingrese su edad: ")
    edad = validar_int(edad, "Ingrese su edad: " )
    
    for partido in lista_partidos:
        partido.mostrar()
    
    numero_de_partidos = input("Ingrese el numero de partido que desea ver: ")
    numero_de_partidos = validar_int(numero_de_partidos, "Ingrese el numero de partido que desea ver: " )
    numero_de_partidos = validar_opciones(numero_de_partidos, 36, "Ingrese el numero de partido que desea ver: ")
    for partido in lista_partidos:
        if partido.number == int(numero_de_partidos):
            part = partido
            break
    tipo_de_entrada =input("Ingrese g si quiere GENERAL o v si quiere VIP: ")
    tipo_de_entrada = validar_string(tipo_de_entrada,  "Ingrese g si quiere GENERAL o v si quiere VIP: " )
    while tipo_de_entrada.lower() != "g" and tipo_de_entrada.lower() != "v":
        tipo_de_entrada = validar_string("1",  "Ingrese g si quiere GENERAL o v si quiere VIP: ")
    if tipo_de_entrada == "g":
        tipo_de_entrada = "GENERAL"
        precio = 35

    if tipo_de_entrada == "v":
        tipo_de_entrada = "VIP"
        precio = 75

    if num_vampiro(int(id)):
        descuento = 0.5 * precio

    else:
        descuento = 0
    iva = precio * 0.16
    total = precio - descuento + iva

    nuevoCliente = Cliente (name, id, edad, tipo_de_entrada)
    nuevoCliente.venta += 1
    lista_clientes.append(nuevoCliente)
    part.venta +=1 
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
    id del boleto= {nuevaentrada.id}

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





