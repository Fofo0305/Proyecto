def gastos_vip(lista_clientes):
    gastos = 0
    for c in lista_clientes:
        if c.tipo_de_entrada == "vip":
            gastos += c.gastos
    print(gastos)

def asistencia_partidos(partidos):
    lista_ordenada = []

    for x in partidos:
        asistencia = x
        for y in partidos:
            if y not in lista_ordenada and y.asistencia > asistencia.asistencia:
                asistencia = y
        lista_ordenada.append(asistencia)

    for partido in lista_ordenada:
        print(f"""
        home = {partido.home}
        away = {partido.away}
        stadium = {partido.stadium}
        boletos_vendidos = {partido.boletos_vendidos}
        asistencia = {partido.asistencia}
        asistencia_entre_venta = {partido.asistencia / partido.venta}
        

""")

def mayor_asistencia (partidos):
    asistencia = partidos[0] 
    for y in partidos:
        if y.asistencia > asistencia.asistencia:
            asistencia = y

def mayor_venta (partidos):
    venta = partidos [0]
    for y in partidos:
        if y.venta > venta.venta:
            venta = y 

def venta_productos (lista_estadios):
    lista_producto = []
    for estadio in lista_estadios:
        for restaurante in estadio.restaurants:
            for producto in restaurante.products:
                lista_producto.append(producto)
    lista_ordenada = []
    for x in lista_producto:
        producto = x
        for y in lista_producto:
            if y not in  lista_ordenada and y.venta > producto.venta:
                producto = y
        lista_ordenada.append(producto)
    print(f""" los e productos con mayor compra son:
          1.- {lista_ordenada[0].name}
          2.- {lista_ordenada [1].name}
          3.- {lista_ordenada [2].name}
          """)
    
def venta_boletos (lista_cliente):
    lista_ordenadas = []
    for cliente in lista_cliente:
        mayor = cliente
        for x in lista_cliente: 
            if x not in lista_ordenadas and x.venta > mayor.venta:
                mayor = x
        lista_ordenadas.append(mayor)
    print(f""" los e productos con mayor compra son:
          1.- {lista_ordenadas[0].name}
          2.- {lista_ordenadas [1].name}
          3.- {lista_ordenadas [2].name}
          """) 









