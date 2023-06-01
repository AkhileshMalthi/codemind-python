def evenindsum(l):
    s = 0
    for i in range(0,len(l),2):
        s+=l[i]
    return s

n = int(input())
nums = list(map(int,input().split()))
evensum = evenindsum(nums)
oddsum = sum(nums)-evensum
print(abs(evensum - oddsum))