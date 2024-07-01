from validaciones import*

def buscarNombre(estadio):
    np = input ("Introduzca el nombre del producto: ")
    #np = validar_string (np,"Introduzca el nombre del producto: ")
    for restaurante in estadio:
        for producto in restaurante.products:
            if np == producto.nombre:
                producto.mostrar()

def buscarTipo(estadio):
    nt = input ("introduzca el nombre del tipo de producto: ")
    nt = validar_string (nt, "introduzca el nombre del tipo de producto: ")
    for restaurante in estadio:
        for producto in restaurante.products:
            if nt == producto.clasificacion:
                producto.mostrar()

def buscar_por_intervalo(estadio):
    pmi = input ("Introduzca el precio minimo que quiera obtener: ")
    pmi = validar_int (pmi, "Introduzca el precio minimo que quiera obtener: " )
    pma = input ("Introduzca el precio maximo que quiera obtener: ")
    pma = validar_int(pma, "Introduzca el precio maximo que quiera obtener: " )
    for restaurante in estadio: 
        for producto in restaurante.products:
            if int(pmi) <= producto.price and int(pma) >= producto.price:
                producto.mostrar()

def comprar(cliente, estadio):
    if cliente == "":
        print("Debe ingresar a un partido")
        return
    compras = []
    for restaurante in estadio.restaurants:
        for producto in restaurante.products:
            if producto.adicional =="alcoholic" and int(cliente.edad) < 18:
                pass
            else:
                producto.mostrar()

    c = input ("Introduzca la comida que desee comprar: ")
    #c = validar_string (c, "Introduzca la comida que desee comprar: " )
    p = 0
    for restaurante in estadio.restaurants:
        for producto in restaurante.products:
            if c == producto.name:
               p = producto
    if p != 0:
        s = input ("Que cantidad de productos desea agregar al carrito: ")
        s = validar_int (s,"Que cantidad de productos desea agregar al carrito: " )
        n = input ("Desea agregar el producto al carrito y proceder a pagar?(s/n): ")
        n = validar_string ( n, "Desea agregar el producto al carrito (s/n): " )
        if n == 's':
            p.venta += int(s)
            for i in range(int(s)):
                compras.append(p)
            price = 0
            iva = 0
            for product in compras:
                price += product.price
                iva += product.price * 0.16 
    if numero_perfecto(int(cliente.id)):
        descuento = price*0.15
    else:
        descuento = 0
    print(f"""
    ci = {cliente.id}
    edad = {cliente.edad}
    productos = {compras} 
    price = {price}
    iva = {iva} 
    descuento = {descuento}
    total = {price - descuento + iva }
""") 
    cliente.gastos += price - descuento + iva
    
def numero_perfecto(ci):
    divisores = []
    for n in range(1,ci):
        if ci % n == 0:
            divisores.append(n)
    if sum(divisores) == ci:
        return True
    return False



               
