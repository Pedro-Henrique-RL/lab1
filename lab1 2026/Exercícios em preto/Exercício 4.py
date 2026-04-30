idade = int(input("Digite a idade da oliveira (em anos): "))

altura_cm = idade * 30
altura_m = altura_cm / 100

print("Altura estimada:", altura_m, "metros")

if altura_m > 5:
    print("Oliveira adulta")
else:
    print("Oliveira em crescimento")
