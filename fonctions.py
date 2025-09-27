def fac(n):
    mult = 1
    if n < 0 :
        return None
    if n == 0 : 
        return 1
    if n > 0 : 
        for i in range(1, n+1):
            mult *= i
    return mult 

def exp(n, k):
    return n**k