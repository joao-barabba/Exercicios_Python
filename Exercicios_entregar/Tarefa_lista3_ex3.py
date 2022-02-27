#3 - Criar um programa que recebe um depósito inicial e a taxa de juros mensal de uma aplicação e imprime os valores, mês a mês , para os 24 primeiros meses. Além disso, escreve o total ganho com os juros do período.

deposito_inicial=float(input('Digite o valor em R$ de deposito inicial: '))
tx_juros=float(input('Digite em porcentagem a taxa de juros mensal'))
c=0

while c<=24:
    valor=deposito_inicial*(1+tx_juros/100)
    print(f'Valor em conta no mês {c} é R${valor:,.2}')
    c+=1
ganhos=valor-deposito_inicial
print(f'Total de ganhos no periodo de 24 meses foi R$ {ganhos:,.2}')    