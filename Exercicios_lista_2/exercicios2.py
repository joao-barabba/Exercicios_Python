#2.Dado o tamanho do lado de um quadrado, calcular a área e o perímetro do mesmo.
lado=(float(input('Digite um lado do seu quadrado: ')))

area=lado*lado
perimetro=lado*2 +lado*2

print(f'A área deste quadrado é : {area:,.2f}\n O perimetro é : {perimetro:,.2f}')