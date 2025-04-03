perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = sum([1 for p in perguntas if input(p + " (s/n): ").strip().lower() == 's'])

if respostas == 5:
    print("Assassino")
elif 3 <= respostas <= 4:
    print("Cúmplice")
elif respostas == 2:
    print("Suspeita")
else:
    print("Inocente")
