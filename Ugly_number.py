def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
n = int(input())
if n==1:
    print("Ugly Number")
else:
    pfs = [x for x in range(2,n+1) if n%x==0 and isprime(x)]
    if pfs.count(2)==0 and pfs.count(3)==0 and pfs.count(5)==0:
        print("Not Ugly Number")
    else :
        print("Ugly Number")