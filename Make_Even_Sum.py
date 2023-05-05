n=int(input())
arr=list(map(int,input().split()))
odds=len([x for x in arr if x%2!=0])
evens=len([x for x in arr if x%2==0])
if evens%2==0 and odds%2==0:
    print(1)
else:
    print(0)