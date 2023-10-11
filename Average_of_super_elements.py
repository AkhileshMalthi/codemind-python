def isSatisfied(n):
    if n == nums.count(n):
        return True
    return False

n = int(input())
nums = list(map(int,input().split()))
result = 0
l = 0
for num in set(nums):
    if isSatisfied(num):
        result += num
        l += 1
if result == 0:
    print(-1)
else:
    print("%.2f" % (result/l))