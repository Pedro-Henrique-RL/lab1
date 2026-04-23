i = 0
maiores = 0

while i < 10:
    idade = int(input("Idade: "))
    if idade >= 18:
        maiores += 1
    i += 1

print("Pessoas com 18 ou mais:", maiores)
