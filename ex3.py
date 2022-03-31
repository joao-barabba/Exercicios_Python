#Escreva um programa que calcule o preço a pagar pela energia elétrica.
#Pergunte a quantidadeconsumida em KWH e o tipo de instalação residencial (R) ou (C) para comercial. Calcule preço pela tabela.
#Residencial <=500 KWh R$0,8 >500 R$0,95
#Comercial <=1000 KWh R$1,10 >1000 R$1,30

instalacao=input("Digite o tipo da sua instalação (C) Comercial e (R) Residencial: ")
kwh=int(input("Quantidade de KWH consumida este mês: "))
valor=0  
if instalacao =="C" or instalacao=="c":
    instalacao="Comercial"
    if kwh<=1000:
        valor=kwh*1.1
    else:
        valor=kwh*1.3

elif instalacao=="R" or instalacao=="r":
    instalacao="Residencial"
    if kwh<=500:
        valor=kwh*0.8
    else:
        valor=kwh*0.95
else:
    print("Tipo de instalação inválida ERRO!!!")
    exit()

print(f"O valor consumidos em sua instalação {instalacao} foi de R$ {valor:.2f}")
