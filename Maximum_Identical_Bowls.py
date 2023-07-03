n = int(input())
arr = list(map(int,input().split()))
while True:
    if sum(arr)%n==0:
        print(n)
        break
    else:
        n = n-1
