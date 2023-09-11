n = int(input())
nums = list(map(int,input().split()))
c = 0
avg = sum(nums)//n
for i in nums:
    if i >= avg:
        c+=1
print(c)