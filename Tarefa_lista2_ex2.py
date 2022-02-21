n1=float(input("Digite um número por favor: "))
n2=float(input("Digite o segundo valor: "))
n3=float(input("Digite o último valor: "))

## Encontrando o menor
if n1<n2:
    if n1<n3:
        menor=n1
    else:
        menor=n3
else:
    if n2<n3:
        menor=n2
    else:
        menor=n3
## Encontrando o maior
if n1>n2:
    if n1>n3:
        maior=n1
    else:
        maior=n3
else:
    if n2>n3:
        maior=n2
    else:
        maior=n3

## Imprimindo na Tela:
print(f"O maior valor é {maior:,.2f} e a menor é {menor:,.2f}")                            