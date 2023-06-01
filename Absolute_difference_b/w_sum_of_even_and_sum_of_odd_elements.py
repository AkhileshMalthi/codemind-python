def evensum(l):
    s = 0
    for i in range(len(l)):
        if l[i]%2==0:
            s+=l[i]
    return s

n = int(input())
nums = list(map(int,input().split()))
evensum = evensum(nums)
oddsum = sum(nums)-evensum
print(abs(evensum - oddsum))