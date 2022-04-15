#1- Criar uma calculadora que execute soma, subtração, multiplicação,
#  divisão e potência de dois números recebidos como parâmetros, utilizando funções no python.
def soma(numero1,numero2):
    r=numero1+numero2
    return(f"{numero1}+{numero2} = {r}")
def subtracao(numero1.numero2):
    r=numero1-numero2
    return(f"{numero1}-{numero2} = {r}")
def multiplicacao(numero1,numero2):
    r=numero1*numero2
    return(f"{numero1}*{numero2} = {r}")
def divisao (numero1,numero2):
    r=numero1/numero2
    return(f"{numero1}/{numero2} = {r}")
   



operacao=input("Qual operação você deseja fazer? ")
numero1=float(input("Insira o 1° valor: "))
numero2=float(input("Insira o 2° valor: "))

calcular(numero1,numero2,operacao)