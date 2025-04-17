i = 0
entre = 0

while i < 10:
    num = int(input(f"Digite o número {i+1}: "))
    if 30 <= num <= 90:
        entre += 1
    i += 1

print("Números entre 30 e 90:", entre)
