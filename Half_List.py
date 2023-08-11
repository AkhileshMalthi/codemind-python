n = int(input())
nums = list(map(int,input().split()))
print(*[*nums[n//2:][::-1],*nums[:n//2]])