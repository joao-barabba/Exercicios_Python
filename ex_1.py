#Faça uma função recursiva para cálculo do MDC

def mdc(a,b):
    return a%b
def calc (a,b):
    if b==0:
        print(a) 
    else:
        print(mdc(a,b))
calc(9,0)

