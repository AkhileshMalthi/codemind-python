n = int(input())
nums = list(map(int,input().split()))
new = list(set(nums))
count = 0
for i in range(len(new)):
    if new[i] == nums.count(new[i]):
        count+=1
print(count)