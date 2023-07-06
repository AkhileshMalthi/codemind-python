def odd(n):
    return n%2!=0

n = int(input())
c = 0
nums = list(map(int,input().split()))
for i in range(1,n-1):
    if odd(nums[i-1]) and odd(nums[i+1]):
        if odd(nums[i]):
            c+=1
print(c)