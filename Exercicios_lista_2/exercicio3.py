#3.Dado o tamanho do raio de uma circunferência, calcular a área e o perímetro da mesma.
raio=(float(input('Digite o raio da circuferência: ')))

area=3.14*(raio*raio)
perimetro=2*3.14*raio

print(f'Sua área é: {area:,.2f} e o perimetro {perimetro:,.2f}')