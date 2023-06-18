n = int(input())
nums = list(map(int,input().split()))
if (sum(nums)//n) in nums:
    print(True)
else:
    print(False)