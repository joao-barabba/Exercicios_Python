def raizI(x,b):
    if b** 2>x:
        return b-1
    return raizI (x,b+1) 
raizI(11,5)