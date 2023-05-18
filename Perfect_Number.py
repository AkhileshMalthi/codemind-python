n=int(input())
l=[x for x in range(1,n) if n%x==0]
if sum(l)==n:
    print(True)
else:
    print(False)