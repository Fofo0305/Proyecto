def gastos_vip(lista_clientes):
    gastos = 0
    for c in lista_clientes:
        if c.tipo_de_entrada == "vip":
            gastos += c.gastos
    print(gastos)

def asistencia_partidos(partidos):
    for partido in partidos:
        print(f"""
        home = {partido.home}
        away = {partido.away}
        stadium = {partido.stadium}do
        boletos_vendidos = {partido.boletos_vendidos}
        asistencia = {partido.asistencia}
        asistencia_entre_venta = {partido.asistencia / partido.venta}
        

""")
