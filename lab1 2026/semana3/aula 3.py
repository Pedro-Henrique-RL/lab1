'''
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")    '''

#Faça um algoritmo para calcular o salário mensal de um funcionário. 
# Sabe-se que o funcionário recebe R$35,00 por hora, faça um algoritmo que leia o total de horas trabalhadas no mês e apresente o salário final. 
# Se o salário for menor que R$1000,00 dê um aumento de R$300,00 no salário recebido, senão apresente somente o resultado da multiplicação.

'''
horas = float(input("Digite as horas trabalhadas do mês:"))
salario = horas * 35

if salario < 1000:
    aumento = salario + 300
    print("Seu salario esse mes é R$",(aumento))
else:
    print("Seu salario esse mes é R$",salario)'''

#Faça um algoritmo que leia dois números distintos e apresente-os em ordem crescente.

'''
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(numero2, numero1)'''

#Faça um algoritmo que leia o ano de nascimento de uma pessoa e verifique se ela pode ou não votar (desconsidere o mês de nascimento).

'''
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar") '''

#Um motorista deseja colocar no seu tanque X reais de gasolina.
#Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.

'''
gasolina = float(input("Escreva o preço da gasolina: "))
pagamento = float(input("Digite quanto será pago: "))
litros = pagamento / gasolina
print("Você colocou {litros} litros de gasolina")'''

#Escreva um algoritmo em Python que dada a idade de uma pessoa, determine sua classificação:
#maior de idade;
#menor de idade;

'''
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")'''

#Leia um número fornecido pelo usuário. Se esse número for positivo, apresente o dobro do valor digitado. 
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido

'''
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print("Numero é par")
else:
    print("Numero é impar")'''

#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde  h corresponde a altura): 
#Homens: (72.7 ∗ h) − 58
#Mulheres: (62, 1 ∗ h) − 44, 7

'''
altura = float(input("digite sua altura: "))
sexo = input("Digite seu sexo: ")

if sexo == "homem":
    peso = (72.7 * altura) - 58
    print("Seu peso ideal é",peso)
    
else:
    peso = (62.1 * altura) - 44.7
    print("Seu peso ideal é", peso)'''

#Peça o valor de uma compra.
#Se o valor for maior que R$100, aplique 10% de desconto.
#Se não, não aplique desconto.

'''
valor = int(input("Digite o valor da compra: "))

if valor > 100:
    desconto = valor * 0.10
    valorF = valor - desconto
    print(valorF)'''
