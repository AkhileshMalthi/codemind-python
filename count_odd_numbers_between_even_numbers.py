def oddoreven(n):
    return True if n%2==0 else False

n = int(input())
nums = list(map(int,input().split()))
count = 0
for i in range(1,n-1):
    if oddoreven(nums[i-1]) == True and oddoreven(nums[i+1]) == True:
        if oddoreven(nums[i]) == False:
            count+=1
print(count)