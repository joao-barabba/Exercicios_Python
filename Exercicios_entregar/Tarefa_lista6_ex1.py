#Criar um programa que armazena 10 nome de pessoas, devem ser inseridas em uma lista e ao final ser exibir todos os nomes.
nomes=['','','','','','','','','','']
x=0
while x <10:
    nomes[x]=str(input('Insira o nome a ser inserido: '))
    x+=1
print(f'Os nomes inseridos foram: {nomes}')
    
    