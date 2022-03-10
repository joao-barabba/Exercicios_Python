#Criar um programa que simula uma urna eletronica simples, no início do programa deve aresentar três candidatos e seus números. A urna deve continuar aceitar votos até digitar encerrar. Ao encerrar a urna deverá indicar o total de votos de cada candidato e o nome do vencedor.
def votacao(candidato):  # fução para votação com a variavel candidato como argumento
    global candidato_bolsonaro, candidato_lula, candidato_doria
 
    if candidato.isalpha():  # checa se candidato contem apenas letras
        if candidato == 'Fim' or candidato == 'fim' or candidato == 'FIM':
            print('FIM DA VOTAÇÃO')
            print_resultados()

    elif candidato.isnumeric():  # checa se candidato e um caracter numerico
        if candidato == '1' or candidato == '2' or candidato == '3':
            if candidato == '1':
                candidato_bolsonaro += 1
            elif candidato == '2':
                 candidato_lula += 1
            elif candidato == '3':
                 candidato_doria += 1
        else:  # se o valor digitado nao e valido, há entrada de novo candidato e a funcao repete
            candidato= str(input('Digite um numero valido para o candidato: '))
            votacao(candidato)


def print_resultados():  # printa resultados e encerra programa
    global candidato_bolsonaro, candidato_lula, candidato_doria

    print('QUANTIDADE DE VOTOS:\n')
    print('CANDIDATO BOLSONARO - TOTAL DE ' + str(candidato_bolsonaro))
    print('CANDIDATO LULA - TOTAL DE ' + str(candidato_lula))
    print('CANDIDATO JOÃO DÓRIA - TOTAL DE ' + str(candidato_doria))

    exit()  # encerra prog


if __name__ == '__main__':  # funcao main 
    candidato_bolsonaro = 0
    candidato_lula = 0
    candidato_doria = 0

    while True:  # laço ocorre indefinidamente ate que ocorra o 'Fim'
        candidato = str(input('ELEIÇÃO ESPECIAL\nDigite o numero do seu candidato: '))
        votacao(candidato)