def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
    
n = int(input())
pfs = [i for i in range(2,n) if n%i==0 and isprime(i)]
if len(pfs)<=1:
    print(-1)
else:
    print(pfs[0],pfs[1])
    