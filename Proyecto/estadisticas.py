def gastos_vip(lista_clientes):
    gastos = 0
    for c in lista_clientes:
        if c.tipo_de_entrada == "vip":
            gastos += c.gastos
    if len(lista_clientes) > 0:
        print(f"El promedio de gastos es de {gastos/len(lista_clientes)}")
    else:
        print("No hay suficientes clientes")

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
        home = {partido.home.name}
        away = {partido.away.name}
        stadium = {partido.stadium.name}
        boletos_vendidos = {partido.venta}
        asistencia = {partido.asistencia}
""")
        if partido.venta == 0:
            print(f"asistencia_entre_venta = 0")
        else:
            
            print(f"asistencia_entre_venta = { partido.asistencia / partido.venta}")
def mayor_asistencia (partidos):
    asistencia = partidos[0] 
    for y in partidos:
        if y.asistencia > asistencia.asistencia:
            asistencia = y
    asistencia.mostrar()
    print(f"CON {asistencia.asistencia} PERSONAS")
def mayor_venta (partidos):
    venta = partidos [0]
    for y in partidos:
        if y.venta > venta.venta:
            venta = y 
    venta.mostrar()
    print(f"CON {venta.venta} BOLETOS VENDIDOS")
    

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
            if producto in lista_ordenada:
                producto = y
            elif y not in  lista_ordenada and y.venta > producto.venta:
                producto = y
        lista_ordenada.append(producto)
    try:
        print(f""" los productos con mayor compra son:
            1.- {lista_ordenada[0].name} con {lista_ordenada[0].venta}
            2.- {lista_ordenada [1].name} con {lista_ordenada[1].venta}
            3.- {lista_ordenada [2].name} con {lista_ordenada[2].venta}
            """)
    except:
        print("No hay suficientes productos vendidos")
    
def venta_boletos (lista_cliente):
    lista_ordenadas = []
    for cliente in lista_cliente:
        mayor = cliente
        for x in lista_cliente:
            if mayor in lista_ordenadas:
                mayor = x 
            elif x not in lista_ordenadas and x.venta > mayor.venta:
                mayor = x
        lista_ordenadas.append(mayor)
    if len(lista_ordenadas)> 2:
        print(f""" los clientes con mayor compra son:
            1.- {lista_ordenadas[0].name} con {lista_ordenadas[0].gastos}
            2.- {lista_ordenadas [1].name} con {lista_ordenadas[1].gastos}
            3.- {lista_ordenadas [2].name} con {lista_ordenadas[2].gastos}
            """) 
    else:
        print("No hay suficientes clientes")









