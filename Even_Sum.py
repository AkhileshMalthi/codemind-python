n = int(input())
nums = list(map(int,input().split()))
s = 0
for i in range(n):
    if nums[i]%2==0:
        s+=nums[i]
print(s)