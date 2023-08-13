n = int(input())
nums = list(map(int,input().split()))
c = 0
for i in range(n):
    if nums[i]%2==0:
        c+=1
print(c,abs(n-c))