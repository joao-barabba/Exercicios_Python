velocidade=float(input("Digite a velocidade em KM/h que você passou no radar: "))
if velocidade>80:
    valor=(velocidade-80)*10
    print(f"Você foi multado no valor de R$ {valor:.2f}")
else:
    print("Parabéns não fez mais que sua obrigação")
    
    