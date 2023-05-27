def isfib(n):
    a = 0
    b = 1
    while a<=n:
        if a == n:
            return True
        c = a+b
        a = b
        b = c
    return False
    
n = int(input())
i = 0
while True:
    if isfib(n-i) and isfib(n+i) and n-i != n+i:
        print(n-i,n+i)
        break
    if isfib(n-i):
        print(n-i)
        break
    if isfib(n+i):
        print(n+i)
        break
    i+=1