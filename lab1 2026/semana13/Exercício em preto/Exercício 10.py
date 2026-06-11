lotes = []

for i in range(5):
    codigo = int(input("Digite um código: "))
    lotes.append(codigo)

buscar = int(input("Digite o código para procurar: "))

encontrado = False

for codigo in lotes:
    if codigo == buscar:
        encontrado = True

if encontrado:
    print("Encontrado")
else:
    print("Não encontrado")
