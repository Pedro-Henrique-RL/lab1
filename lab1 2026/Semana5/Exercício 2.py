# EXERCÍCIO 2

f1 = float(input("Força 1: "))
f2 = float(input("Força 2: "))
f3 = float(input("Força 3: "))

if f1 + f2 > f3 and f1 + f3 > f2 and f2 + f3 > f1:
    print("Há equilíbrio")

    if f1 == f2 and f2 == f3:
        print("Simétrico")
    elif f1 == f2 or f1 == f3 or f2 == f3:
        print("Parcialmente simétrico")
    else:
        print("Assimétrico")
else:
    print("Não há equilíbrio")
