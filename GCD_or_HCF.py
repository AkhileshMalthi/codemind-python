a,b = map(int,input().split())
i = min(a,b)
while i>0:
    if a%i==0 and b%i==0:
        break
    i-=1
print(i)