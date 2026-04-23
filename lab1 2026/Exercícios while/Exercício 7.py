i = 0
a = 0
b = 0
c = 0

while i < 10:
    voto = input("Bebida (A-Expresso, B-Cappuccino, C-Chá): ").upper()

    if voto == "A":
        a += 1
    elif voto == "B":
        b += 1
    elif voto == "C":
        c += 1

    i += 1

print("Expresso:", a, "-", (a/10)*100, "%")
print("Cappuccino:", b, "-", (b/10)*100, "%")
print("Chá:", c, "-", (c/10)*100, "%")
