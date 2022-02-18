valorProduto=float(input('Digite o valor do produto:'))
desconto=float(input('\nDigite a porcentagem de desconto:'))
valorPagamento= valorProduto-(desconto/100)*valorProduto
print('Valor original era de R$ {} foi aplicado um desconto de {}%, eo novo valor agora é R${}'.format(valorProduto, desconto ,valorPagamento))