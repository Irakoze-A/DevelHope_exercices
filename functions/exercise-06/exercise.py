def fibo(n):
    if n == 0:
        return 0
    if n == 1 :
        return 1
     
    return fibo(n-1)+ fibo(n-2)


liste = [fibo(n) for n in range(5)]

print(liste)
    