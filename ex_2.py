#Faça uma função recursiva para calcular o fatorial de um número
def fatorial(x):
    return x-1

def entrada():
    x=int(input("digite um número: ")) 
    while x>=1:
        print(fatorial(x))
        x-=1
entrada()

