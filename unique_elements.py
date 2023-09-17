n = int(input())
nums = list(map(int,input().split()))
unq = []
for i in nums:
    if i not in unq:
        unq.append(i)
print(*unq)