n=27632120
def contar(n,k):
    count=0
    while n>0:
        if n%10==k:
            count+=1
        n=n//10
    return count    
contar(n,2)