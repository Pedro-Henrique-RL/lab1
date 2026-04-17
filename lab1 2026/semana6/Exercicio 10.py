numero_oliveiras = 37

tentativa = -1 
while tentativa != numero_oliveiras:
    tentativa = int(input("Tente adivinhar o número de oliveiras (1 a 100): "))

    if tentativa < numero_oliveiras:
        print("Há mais oliveiras, tente um número maior.")
    elif tentativa > numero_oliveiras:
        print("Há menos oliveiras, tente um número menor.")
    else:
        print("Parabéns! Você descobriu a quantidade de oliveiras!")
