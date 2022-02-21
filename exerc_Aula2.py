altura=float(input("Digite sua altura: "))
peso=float(input("Digite seu peso: "))

imc=peso/(altura*altura)
if imc<18.5:
        print("Abaixo do peso")
if imc>=18.5 and imc<25:
        print("Peso normal")
if imc>=24.9 and imc<30:
        print("Sobrepeso")
if imc>=29.9 and imc<35:
        print("Obesidade 1")
if imc>=34.9 and imc<40:
        print("Obesidade 2")
if imc>40:
        print("Obesidade 3")
