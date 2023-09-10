input()
nums = list(map(int,input().split()))
newNums = []
for i in nums:
    if i%2!=0:
        newNums.append(i)
for i in nums:
    if i%2==0:
        newNums.append(i)
print(*newNums)