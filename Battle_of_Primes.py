def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True

a = int(input())
b = int(input())
i = a+b+1
while True:
    if isprime(i):
        break
    else:
        i+=1
print(i-(a+b))