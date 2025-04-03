nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
frequencia = float(input("Digite a frequência (%): "))

media = (nota1 + nota2) / 2

if media >= 7.0 and frequencia >= 75:
    print("Aprovado")
elif 4.0 <= media < 7.0 and frequencia >= 75:
    print("Exame")
else:
    print("Reprovado")
