codigos = []

for i in range(5):
    codigo = int(input("Digite um código: "))
    codigos.append(codigo)

distintos = True

for i in range(len(codigos)):
    for j in range(i + 1, len(codigos)):
        if codigos[i] == codigos[j]:
            distintos = False

if distintos:
    print("Distintos")
else:
    print("Há duplicatas")
