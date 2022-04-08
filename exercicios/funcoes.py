'''from ast import Return


def somar(a,b):
    return(a+b)
somar(1,2)'''
'''
def  epar(x):
    return x % 2 ==0
def par_ou_impar(x):    
    if epar(x):
        return "par"
    else:
        return "impar"
'''        ''' 
def maior(a,b):
    if a>b:
        print(a)
    else:
        print(b)      
maior(25,6)
'''
'''
def fatorial(x):
    if x == 0 or x==1:
        return 1
    else:
        return x * fatorial(x-1)
        
       
fatorial(3)
'''
'''
def barra(n=40, caractere="*"):
    print(caractere*n)

barra(15)
'''
def retangulo(largura,altura,caractere ="+"):
    linha= caractere*largura
    for i in range(altura):
        print(linha)
retangulo(18,10)        