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
total=0# total de votos começa negativos pois tem o input FIM para encerrar o programa
maior=0



def votacao (voto): ## Declarando função para a votação
    global windows, unix, linux, netware,mac,outros,outrosPersent,windowsPersent,unixPersent,linuxPersent,netwarePersent,macPersent,total
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
            total-=1
            votacao(voto)
def verify():
    global max_idx,idx,num,x,nomeSistema,sistemas,windows,unix,linux,netware,mac,outros,outrosPersent,windowsPersent,unixPersent,linuxPersent,netwarePersent,macPersent,total,indexLista,persentLista
    max_value = None
    max_idx = None
    x=0
    num=0
    sistemas=[windows,unix,linux,netware,mac,outros]
    indexLista=['windows','unix','linux','netware','mac','outros']


    for idx, num in enumerate(sistemas):
        if (max_value is None or num > max_value):
            max_value = num
            max_idx = idx
    nomeSistema=indexLista[max_idx]
    



def print_resultados():#Printando Resultados Ordenando e encerrando o programa
    global num,nomeSistema,sistemas,windows,unix,linux,netware,mac,outros,outrosPersent,windowsPersent,unixPersent,linuxPersent,netwarePersent,macPersent,total,indexLista,persentLista
    windowsPersent=(windows*100)/total
    unixPersent=(unix*100)/total
    linuxPersent=(linux*100)/total
    netwarePersent=(netware*100)/total
    macPersent=(mac*100)/total
    outrosPersent=(outros*100)/total
                                  
    sistemas=[windows,unix,linux,netware,mac,outros]
    indexLista=['windows','unix','linux','netware','mac','outros']
    persentLista=[windowsPersent,unixPersent,linuxPersent,netwarePersent,macPersent,outrosPersent]
    print(f"Windows quantidade de votos {sistemas[0]} porcentagem  % {windowsPersent:.2f}")
    print(f"Unix quantidade de votos {sistemas[1]} porcentagem  % {unixPersent:.2f}")
    print(f"Linux quantidade de votos {sistemas[2]} porcentagem  % {linuxPersent:.2f}")
    print(f"Netware quantidade de votos {sistemas[3]} porcentagem  % {netwarePersent:.2f}")
    print(f"Mac Os quantidade de votos {sistemas[4]} porcentagem  % {macPersent:.2f}")
    print(f"Outros quantidade de votos {sistemas[5]} porcentagem  % {outrosPersent:.2f}\n")
    print(f"O total de votos foi {total}")
    
    verify()
    sistemas.sort()#Coloca em ordem crescente o sistema que teve mais votos ao que teve menos votos
    sistemas.sort(reverse=True)
    persentLista.sort()#Coloca em ordem crescente o sistema que teve mais votos ao que teve menos votos
    persentLista.sort(reverse=True)
    print(f"O servidor vencedor é {nomeSistema} com {sistemas[0]} de votos e com %{persentLista[0]:.2f} do total de votos")
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
        total+=1 
