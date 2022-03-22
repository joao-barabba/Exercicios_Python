ultimo=10
fila=list(range(1,ultimo+1))#Função Sequenciadora de 1 para ultimo +1
fila2=list(range(1,ultimo+1))
while True:# Sempre dará verdadeiro em loop e só sairá no break
    print(f"Existem{len(fila)} clientes na fila\n")
    print(f"Existem{len(fila2)} clientes na fila\n")
    print(f"Fila atual: {fila}\n")
    print(f"Fila atual: {fila2}\n")
    print("Digite a Fila que deseja atualizar 1 ou a 2: ")
    choice=input("Escolha (1) ou (2): )")
    if choice=="1":
        print("Digite F para adicionar no final da fila,")
        print(f"A para realizar o atendimento ou S para sair")
        operacao= input("Operação (F,A ou S): ")
        if operacao == "A" or operacao=="a":
            if len (fila)>0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia!!!")
        elif operacao == "F" or operacao=="f":
            ultimo+=1
            fila.append(ultimo)
        elif operacao =="S" or operacao =="s":
            break    
        else:
            print("Operação inválida !")
    elif choice=="2":
        print("Digite F para adicionar no final da fila,")
        print(f"A para realizar o atendimento ou S para sair")
        operacao= input("Operação (F,A ou S): ")
        if operacao == "A" or operacao=="a":
            if len (fila2)>0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia!!!")
        elif operacao == "F" or operacao=="f":
            ultimo+=1
            fila.append(ultimo)
        elif operacao =="S" or operacao =="s":
            break    
        else:
            print("Operação inválida !")            
