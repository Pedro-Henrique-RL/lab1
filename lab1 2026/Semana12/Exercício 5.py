
def aprovado():
    print("Aluno aprovado")

def recuperacao():
    print("Aluno em recuperação")

def reprovado():
    print("Aluno reprovado")

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))
n5 = float(input("Digite a nota 5: "))

media = (n1 + n2 + n3 + n4 + n5) / 5

print("Média:", media)

if media >= 7:
    aprovado()

elif media >= 4 and media < 7:
    recuperacao()

else:
    reprovado()
