def ex5():
    a = []
    b = []
    for i in range(5):
        a.append(int(input(f"A[{i}]: ")))
    for i in range(5):
        b.append(int(input(f"B[{i}]: ")))
    c = []
    for i in range(5):
        c.append(a[i] + b[i])
    print("Soma:", c)
