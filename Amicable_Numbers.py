n = int(input())
m = int(input())
nfs = [x for x in range(1,n) if n%x==0]
mfs = [x for x in range(1,m) if m%x==0]
if sum(nfs) == m and sum(mfs) == n:
    print("Amicable")
else: 
    print("Not Amicable")