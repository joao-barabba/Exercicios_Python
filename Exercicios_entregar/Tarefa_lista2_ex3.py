n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
o=(input('Digite o operador para conta: '))

if o=='+':
    r=n1+n2
    print(f'O resultado da conta é {r:,}')
elif o=='-':
    r=n1-n2
    print(f'O resultado da conta é {r:,}')
elif o=='*':
    r==n1*n2
    print(f'O resultado da conta é {r:,}')
elif o=='/':
    r==n1/n2
    print(f'O resultado da conta é {r:,}')
else:
    print('Operador não reconhecido ERRO!!!')       
       