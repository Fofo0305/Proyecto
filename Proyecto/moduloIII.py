from modulo_II import *

def validar_boleto (lista_clientes):
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
                entrada.partido.asistencia +=1
                print("BIENVENIDO")
                return entrada, usuario
    print("NO SE ENCONTRO UNA ENTRADA VALIDA")