n = int(input())
nums = list(map(int,input().split()))
count = 0
for i in range(n):
    if i == 0:
        if (nums[n-1]%2==0 and nums[i+1]%2!=0 or nums[n-1]%2!=0 and nums[i+1]%2==0):
            count+=1
    elif i == n-1:
        if (nums[0]%2==0 and nums[i-1]%2!=0 or nums[0]%2!=0 and nums[i-1]%2==0):
            count+=1
    else :
        if (nums[i-1]%2==0 and nums[i+1]%2!=0 or nums[i-1]%2!=0 and nums[i+1]%2==0):
            count+=1
print(count)