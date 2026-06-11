rfid = []

while len(rfid) < 10:
    codigo = int(input("Digite um código maior que 1000: "))

    if codigo > 1000:
        rfid.append(codigo)
    else:
        print("Código inválido!")

print("Códigos cadastrados:")
print(rfid)
