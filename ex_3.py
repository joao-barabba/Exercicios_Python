#Faça um função recursiva que calcule n-ésimo termo da sequência Fibonacci
def fib(n):
    if n<2:
        print(n)
    else:
        print((n-1) +(n-2))
        
         
fib(12)   