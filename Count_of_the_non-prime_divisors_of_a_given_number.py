def isnotprime(n):
    if n==1: return True
    for i in range(2,(n//2)+1):
        if n%i==0:
            return True
    return False

n = int(input())
divs = [i for i in range(1,n+1) if n%i==0 and isnotprime(i)]
print(len(divs))