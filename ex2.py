# 2- Criar um programa que recebe um número e indica se é par ou impar

valor=int(input("Digite o valor: "))
resto=valor%2
if resto==0:
    print("Número é par")
else:
    print("Impar")    
