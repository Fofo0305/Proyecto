

def buscarNombre(estadio):
    np = input ("Introduzca el nombre del producto: ")
    for restaurante in estadio:
        for producto in restaurante.products:
            if np == producto.nombre:
                producto.mostrar()

def buscarTipo(estadio):
    nt = input ("introduzca el nombre del tipo de producto: ")
    for restaurante in estadio:
        for producto in restaurante.products:
            if nt == producto.clasificacion:
                producto.mostrar()

def buscar_por_intervalo(estadio):
    pmi = input ("Introduzca el precio minimo que quiera obtener: ")
    pma = input ("Introduzca el precio maximo que quiera obtener: ")
    for restaurante in estadio: 
        for producto in restaurante.products:
            if pmi <= producto.price and pma >= producto.price:
                producto.mostrar()

def comprar(cliente, estadio):
    if cliente == "":
        print("Debe ingresar a un partido")
        return
    edad = input ("Introduzca su edad: ")
    compras = []
    for restaurante in estadio:
        for producto in restaurante.products:
            if producto.adicional =="alcoholic" and edad < 18:
                pass
            else:
                producto.mostrar()

    c = input ("Introduzca la comida que desee comprar: ")
    p = 0
    for restaurante in estadio:
        for producto in restaurante.products:
            if c == producto.nombre:
               p = producto
    if p != 0:
        s = input ("Que cantidad de productos desea agregar al carrito: ")
        n = input ("Desea agregar el producto al carrito (s/n): ")
        if n == 's':
            for i in range(s):
                compras.append(p)
            price = 0
            iva = 0
            for product in compras:
                price += product.price
                iva += product.price * 0.16 
    if numero_perfecto(cliente.cedula):
        descuento = price*0.15
    else:
        descuento = 0
    print(f"""
    ci = {cliente.cedula}
    edad = {edad}
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







               
