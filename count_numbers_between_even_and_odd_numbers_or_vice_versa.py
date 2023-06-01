def iseven(n):
    return True if n%2==0 else False
    

n = int(input())
nums = list(map(int,input().split()))
count = 0
for i in range(1,n-1):
    if iseven(nums[i-1]) == True and iseven(nums[i+1]) == False:
        count+=1
    elif iseven(nums[i-1]) == False and iseven(nums[i+1]) == True:
        count+=1
    else :
        continue
print(count)