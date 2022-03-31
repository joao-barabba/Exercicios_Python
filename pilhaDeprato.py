import os
from turtle import clear
prato=5
pilha=list(range(1,prato+1))



while True:
    print(f"Existem{len(pilha)} pratos na pilha ")
    print(f"Pilha atual: {pilha}")
    print(f"Digite E para empilhar um prato,")
    print(f"D para desempilhar ou S para sair")
    
    operacao=input("Operação (E , D ou S): ")
    if operacao == "D" or operacao=="d":
        if len(pilha)>0:
            lavado=pilha.pop(-1)
            print(f"Prato(s) {lavado} lavado(s)")
        else:
            print("Pilha vazia! Nada para lavar")
    elif operacao=="E" or operacao=="e":
        prato+=1
        pilha.append(prato)
    elif operacao=="S" or operacao=="s":
        break
    else:
        print("Operação inválida! Digite E, D ou S em seu teclado.")                