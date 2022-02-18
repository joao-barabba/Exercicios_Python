salarioAntigo=float(input('Digite o seu antigo salário por favor:'))
aumento=float(input('Digite a porcentagem de aumento no seu salário:'))
salarioNovo=salarioAntigo+(aumento/100)*salarioAntigo
print('Seu novo salário será R${}'.format(salarioNovo))