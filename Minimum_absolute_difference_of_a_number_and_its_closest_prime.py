def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True

n = int(input())
i = 0
while True:
    if isprime(n-i):
        print(abs(n-(n-i)))
        break
    if isprime(n+i):
        print(abs(n-(n+i)))
        break
    i+=1
