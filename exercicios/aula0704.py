#Exercicio
#1- Criar um programa que recebe um nome e o armazena em um arquivo. Cada nome deve estar em uma linha do arquivo.
# O programa deve continuaraceitando nomes até digitar "0"
arquivo=open("listagem.txt","a")
while True:
    nome=input("Digite o nome para escrever no arquivo ou 0 para sair: ")
    if nome == "0":
        print("Você fechou o programa")
        break
    else:    
        arquivo.write(f"{nome}\n")     
arquivo.close