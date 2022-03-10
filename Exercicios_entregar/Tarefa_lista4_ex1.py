#1-Escreva um programa que controla uma máquina registradora simples.Você deve solicitar um código de produto e uma quantidade ao usuário e no final deve imprimir o total das compras. Os códigos são 001 - R$2,50, 002 - R$7,00 , 003 - R$4,00.


print('Bem vindo ao super mercado dev favor responder as seguintes questões: ')
produto=input('Digite o código do produto: ')

if produto =='001':
    qtd=int(input('Quantas unidades o cliente quer: '))
    valor=qtd*2.5
    print(f'Valor da compra é de R$ {valor:.2f}')
elif produto =='002':
    qtd=int(input('Quantas unidades o cliente quer: '))
    valor=qtd*7
    print(f'Valor da compra é de R$ {valor:.2f}')
elif produto =='003':
    qtd=int(input('Quantas unidades o cliente quer: '))
    valor=qtd*4
    print(f'Valor da compra é de R$ {valor:.2f}')
else:
    print('ERRO!Código não encontrado no banco de dados:')
    

