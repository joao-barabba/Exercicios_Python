arquivo=open("listagem.txt","r")
nome=input("Qual nome consultar: ") +"\n"

conteudo = arquivo.readlines()
if nome in conteudo:
    print(f"O nome {nome} pertence a lista")
else:
    print(f"O nome {nome} não pertence a lista")
    
arquivo.close()
