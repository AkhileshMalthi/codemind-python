n = int(input())
nums = list(map(int,input().split()))
unq = [i for i in nums if nums.count(i) == 1]
print(max(unq)) if unq != [] else print(-1)