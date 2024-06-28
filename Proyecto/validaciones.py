def validar_string(x, msg):
    while not x.isalpha():
        x = input(msg)
    return x

def validar_int(x, msg):
    while not x.isnumeric():
        x = input(msg)
    return x


def validar_opciones(x, max, msg):
    while not x.isnumeric() or int(x) > max:
        x = input(msg)
    return int(x)

