from modulo_II import *

def validar_boleto ():
    cd = input ("escribir su Cedula de identidad :") 
    id_b = input ("escribir id del boleto :")
    usuario = 0
    for cliente in lista_clientes:
        if cd == cliente.id:
            usuario = cliente

    if usuario !=0:
        for entrada in usuario.entradas:
            if id_b == entrada.id and entrada.valida:
                entrada.valida = False
                print("BIENVENIDO")
                return
    print("NO SE ENCONTRO UNA ENTRADA VALIDA")