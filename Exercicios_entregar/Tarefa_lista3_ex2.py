#2 - Criar um programa que pergunta qauntos números você quer utilizar,  em seguida, recebe cada um dos números e imprime a média entre eles
from re import match


divisor=int(input('Digite a quantidade de números que quer usar: '))
count=divisor
num=0
while count!=0:
    num=float(input('Digite o número: '))
    num_final=(num+num)
    count-=1
    
media=num_final/divisor    
print(media)    

