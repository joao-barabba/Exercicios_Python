'''

x=5
def verificar():
    listaNomes=['']
    while True:
        if x==0:
            listaNomes= [input(print("Digite um nome: "))]
            x-=1
        else:
            print("Obrigado")
            break
verificar()
print(listaNomes)        
'''

#Variáveis em funções
#Variáveis -> Globais ou externas -> locais ou internas
'''
nome= "Pedro Rocha"
def imprime():
    print("*"*len(nome))

a= 5
def muda_e_imprime():
    global a
    a=7
    print(f"Variável a dentro da função: {a}")
print(f"Variável antes de mudar: {a}")
muda_e_imprime()
print(f"Variável após a mudança: {a}")  
''' 
'''
valor=int(input("Digite ae seu merda: "))
def faixa_int(minimo,maximo):
    while True:
        v= valor
        if v < minimo or v>maximo:
            print(f"Valor inválido. Digite um valor entre {minimo} e {maximo}")
            break
        else:
            print(f"{v} OK")
            break    
faixa_int(1,100)
'''
def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def imprime(a,b,funcao):
    print(funcao(a,b))  
imprime(5,4,soma)
imprime(10,1,subtracao)