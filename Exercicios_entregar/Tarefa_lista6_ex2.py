#2 - Criar um programa que pergunta quantos nomes de pessoas serão inseridos, armazena esses nomes, que devem
# ser inseridos em uma lista e ao final, impressos
nome=[]
a=0
count=int(input('Quantos nome você quer adicionar nesta lista? '))
x=0
while x<count:
    a=str(input('Escreva um nome: '))
    nome.append(a)#Adiciona ao fim da lista a variavel a
    x+=1
x=0
while x<count:
    print(nome[x])
    x+=1     
#nome=[]
#a = 0
#count=int(input('Quantos nome você quer adcionar nesta lista? '))
#x=0
#while x < count:
#    a = input("Escreva um nome: ")
#    nome.append(a)
#    x+=1
#x=0
#print(nome)
#while x < count:
#    print(nome[x])
#    x+=1