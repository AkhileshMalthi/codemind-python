def iseven(n):
    return True if n%2==0 else False

n = int(input())
nums = list(map(int,input().split()))
num = 0
for i in range(n):
    if iseven(nums[i]):
        num = nums[i]
print(num)