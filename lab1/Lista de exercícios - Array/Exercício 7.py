import random

def ex7():
    vetor = []
    for _ in range(10):
        vetor.append(random.randint(1, 100))
    print("Pares:", [n for n in vetor if n % 2 == 0])
