#Criar um programa que recebe um número e imprime a tabuada desse número, até dez. No modelo: 2 x 1 = 2, 2 x 2 = 4, etc...
num=int(input('Digite o número que deseja saber a tabuada: '))
c=1
while c<=10:
    res=c*num
    print(f'{num}x{c}={res}')
    c+=1