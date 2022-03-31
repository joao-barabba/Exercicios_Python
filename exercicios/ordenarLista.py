#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: "Qual o melhor Sistema Operacional para uso em servidores?" As possíveis respostas são: 1- Windows 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro • Você deve desenvolver um programa em Python que receba as respostas da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0 (zero), que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados em uma lista. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada uma das respostas e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e de ser feito segundo o exemplo:
'''
Sistemas Operacionais - Votos %
Windows - 1500 -17%
Unix - 3500 40%
Linux - 3000 - 34%
Netware – 500 - 5%
Mac OS - 150 - 2%
Outro - 150 - 2%

Total de 8800 votos
O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''
sistemas=[0]
count=0

def votacao (voto): ## Declarando função para a votação
    global windows, unix, linux, netware,mac,outros  
    if voto.isalpha():
        if voto == "FIM" or voto == "fim" or voto == "Fim":
            print("Votação encerrada!")
            print_resultados()
    elif voto.isnumeric():
        if voto == "1" or voto =="2" or voto =="3" or voto =="4" or voto == "5" or voto == "6":
            if voto=="1":
                windows+=1
            elif voto=="2":
                unix+=1
            elif voto=="3":
                linux+=1
            elif voto=="4":
                netware+=1
            elif voto=="5":
                mac+=1
            elif voto=="6":
                outros+=1
        else:
            voto=input("Valor não reconhecido, Digite um valor válido para votação :  ")
            votacao(voto)
def print_resultados():#Printando Resultados Ordenando e encerrando o programa
    global windows,unix,linux,netware,mac,outros                              
    sistemas[0]=windows
    sistemas[1]=unix
    sistemas[2]=linux
    sistemas[3]=netware
    sistemas[4]=mac
    sistemas[5]=outros
    print(sistemas)
    exit()
if __name__ == '__main__':  # funcao main 
    windows = 0
    unix = 0
    linux = 0
    netware = 0
    mac = 0
    outros = 0              
    while True:
        voto=input("Qual o melhor Sistema Operacional para uso em servidores?\n 1- Windows 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro: \n")
        votacao(voto)


    