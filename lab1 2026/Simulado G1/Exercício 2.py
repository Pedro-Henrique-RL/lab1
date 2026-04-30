dia = -1

while dia < 1 or dia > 365:
    dia = int(input("Digite um dia juliano (1 a 365): "))
    
    if dia < 1 or dia > 365:
        print("Valor inválido, tente novamente.")

if dia <= 59:
    print("1º bimestre")
elif dia <= 120:
    print("2º bimestre")
elif dia <= 181:
    print("3º bimestre")
elif dia <= 243:
    print("4º bimestre")
elif dia <= 304:
    print("5º bimestre")
else:
    print("6º bimestre")
