def isodd(n):
    return False if n%2==0 else True

n = int(input())
nums = list(map(int,input().split()))
ind = 0
for i in range(n):
    if isodd(nums[i]):
        ind = i
print(ind)