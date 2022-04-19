#Somar os valores da lista


lista = [1,5,7,2,26,3]

def soma(lista,indice):
    if indice == -1:
        return 0
    return  lista[indice] + soma(lista,indice-1)
soma(lista,5)

    
