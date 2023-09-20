n = int(input())
nums = list(map(int,input().split()))
count = 0
for num in set(nums):
    if nums.count(num) == num:
        count+=1
print(count)