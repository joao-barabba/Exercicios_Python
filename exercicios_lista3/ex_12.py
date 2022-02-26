#Difícil  12-  Fabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do salário bruto,ça  um  programa  para  o  cálculo  de  uma  folha  de  pagamento,  sabendo  que  os  descontos são do imposto de Renda, que depende do salário bruto (conforme ta mas não é descontado (é a empresa que deposita.) O salário líquido corresponde ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.Desconto do IR: •Salário Bruto ate R$900,00 (inclusive) – Isento;•Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;•Salário bruto até R$ 2500,00 (Inclusive) – desconto de 10%;•Salário bruto acima de 2500 – Desconto de 20%.  Imprima  na  tela  as  informações,  dispostas  conforme  o  exemplo  abaixo,  no  exemplo  valor  da  hora é 5 e a quantidade de horas é 220.Salário bruto (5 * 220)           : R$   1100,00( – ) IR (5%)                     : R$     55,00( – ) INSS ( 10% )                : R$    110,00 FGTS ( 11%)                       : R$    121,00Total de descontos                : R$    165,00Salário Líquido                   : R$    935,00 

valor_hora=float(input('Digite o valor da sua hora trabalhada: '))
qtd_horas=float(input('Digite quantas horas trabalhadas no mês: '))

salario_bruto=valor_hora*qtd_horas
inss=salario_bruto*0.1
fgts=salario_bruto*0.11

if salario_bruto<=900:
    ir=0
    desconto= ir+inss
    salario_liquido=salario_bruto-desconto
    print(f'Salário Bruto R$ {salario_bruto:,.2f}')
    print(f'Imposto de renda R$ {ir:,.2f}')
    print(f'INSS R$ {inss:,.2f}')
    print(f'FGTS R$ {fgts:,.2f}')
    print(f'Total de descontos R$ {desconto:.2f}')
    print(f'Salário Liquido R$ {salario_liquido:,.2f}')
elif salario_bruto<=1500:
    ir=salario_bruto*0.05
    desconto=ir+inss
    salario_liquido=salario_bruto-desconto
    print(f'Salário Bruto R$ {salario_bruto:,.2f}')
    print(f'Imposto de renda R$ {ir:,.2f}')
    print(f'INSS R$ {inss:,.2f}')
    print(f'FGTS R$ {fgts:,.2f}')
    print(f'Total de descontos R$ {desconto:.2f}')
    print(f'Salário Liquido R$ {salario_liquido:,.2f}')
elif salario_bruto<=2500:
    ir=salario_bruto*0.1
    desconto=ir+inss
    salario_liquido=salario_bruto-desconto
    print(f'Salário Bruto R$ {salario_bruto:,.2f}')
    print(f'Imposto de renda R$ {ir:,.2f}')
    print(f'INSS R$ {inss:,.2f}')
    print(f'FGTS R$ {fgts:,.2f}')
    print(f'Total de descontos R$ {desconto:.2f}')
    print(f'Salário Liquido R$ {salario_liquido:,.2f}')
else:
    ir=salario_bruto*0.2
    desconto=ir+inss
    salario_liquido=salario_bruto-desconto
    print(f'Salário Bruto R$ {salario_bruto:,.2f}')
    print(f'Imposto de renda R$ {ir:,.2f}')
    print(f'INSS R$ {inss:,.2f}')
    print(f'FGTS R$ {fgts:,.2f}')
    print(f'Total de descontos R$ {desconto:.2f}')
    print(f'Salário Liquido R$ {salario_liquido:,.2f}')   
