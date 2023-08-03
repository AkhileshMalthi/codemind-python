n = int(input())
nums = list(map(int,input().split()))
snums = sorted(nums)
count = 0
for i in range(n):
    if nums[i] != snums[i]:
        idx = nums.index(snums[i])
        nums[i],nums[idx] = nums[idx],nums[i]
        count+=1
print(count)
        