def isprime(n):
    if n == 1:
        return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True


a = int(input())
b = int(input())
primes = list(filter(isprime,range(a,b+1)))
for i in primes:
    print(i)
