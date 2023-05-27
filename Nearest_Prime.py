def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True

t = int(input())
for tc in range(t):
    n = int(input())
    i = 0
    while True:
        if isprime(n-i):
            print(n-i)
            break
        if isprime(n+i):
            print(n+i)
            break
        i+=1


    