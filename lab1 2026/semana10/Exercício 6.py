
a = 0
b = 0
c = 0

for i in range(20):

    jornal = input("Digite o jornal (A, B ou C): ")

    if jornal == "A":
        a = a + 1
    elif jornal == "B":
        b = b + 1
    elif jornal == "C":
        c = c + 1

porcentagem_a = (a / 20) * 100
porcentagem_b = (b / 20) * 100
porcentagem_c = (c / 20) * 100

if porcentagem_a <= porcentagem_b and porcentagem_a <= porcentagem_c:

    print("A =", porcentagem_a, "%")

    if porcentagem_b <= porcentagem_c:
        print("B =", porcentagem_b, "%")
        print("C =", porcentagem_c, "%")
    else:
        print("C =", porcentagem_c, "%")
        print("B =", porcentagem_b, "%")

elif porcentagem_b <= porcentagem_a and porcentagem_b <= porcentagem_c:

    print("B =", porcentagem_b, "%")

    if porcentagem_a <= porcentagem_c:
        print("A =", porcentagem_a, "%")
        print("C =", porcentagem_c, "%")
    else:
        print("C =", porcentagem_c, "%")
        print("A =", porcentagem_a, "%")

else:

    print("C =", porcentagem_c, "%")

    if porcentagem_a <= porcentagem_b:
        print("A =", porcentagem_a, "%")
        print("B =", porcentagem_b, "%")
    else:
        print("B =", porcentagem_b, "%")
        print("A =", porcentagem_a, "%")
