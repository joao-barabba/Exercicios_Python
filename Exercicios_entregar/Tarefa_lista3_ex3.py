#3 - Criar um programa que recebe um depósito inicial e a taxa de juros mensal de uma aplicação e imprime os valores, mês a mês , para os 24 primeiros meses. Além disso, escreve o total ganho com os juros do período.

deposito_inicial=float(input('Digite o valor em R$ de deposito inicial: '))
tx_juros=float(input('Digite em porcentagem a taxa de juros mensal: '))
mes=0
calc=tx_juros/100
valor_atual=deposito_inicial

while mes<=24:
    valor_juros=valor_atual*calc
    valor_atual=valor_atual+valor_juros
    print(f'Valor em conta no mês {mes} é R${valor_atual:.2f}')
    mes+=1
ganhos=valor_atual-deposito_inicial
print(f'Total de ganhos no periodo de 24 meses foi R$ {ganhos:.2f}')    