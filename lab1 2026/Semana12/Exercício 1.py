
def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

def verificar_aprovacao(media):
    if media >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

resultado = calcular_media(nota1, nota2)

print("Média:", resultado)

verificar_aprovacao(resultado)
