
def converter_hora(hora, minuto):

    if hora == 0:
        hora12 = 12
        periodo = "AM"

    elif hora < 12:
        hora12 = hora
        periodo = "AM"

    elif hora == 12:
        hora12 = 12
        periodo = "PM"

    else:
        hora12 = hora - 12
        periodo = "PM"

    return hora12, minuto, periodo

def mostrar_hora(hora12, minuto, periodo):
    print(f"{hora12}:{minuto:02d} {periodo}")

hora = int(input("Digite a hora (0 até 23): "))
minuto = int(input("Digite os minutos (0 até 59): "))

h, m, p = converter_hora(hora, minuto)

mostrar_hora(h, m, p)
