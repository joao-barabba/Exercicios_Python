##2 - Escreva um programa que exiba uma lista de opções (menu):adição, subtração, divisão, multiplicação e ao sair imprima a tabuada da operação escolhida

print('Bem vindo ao nosso menu favor selecionar a operação escolhida conforme o número que o acompanha...')

operacao=input('1- Adição 2- Subtração 3- Divisão 4- Multiplicação :  ')
num=int(input('Digite um número para na saída ter a tabuada: '))
c=1

if operacao=='1':
    while c<=10:
    res=c+num
    print(f'{num}+{c}={res}')
    c+=1
elif operacao=='2':
    while c<=10:
    res=c-num
    print(f'{num}-{c}={res}')
    c+=1
elif operacao=='3':
    while c<=10:
    res=c/num
    print(f'{num}/{c}={res}')
    c+=1
elif operacao=='4':
    while c<=10:
    res=c*num
    print(f'{num}x{c}={res}')
    c+=1
else:
    print('ERRO! Operação não registrada')
    
