def oddpossum(l):
    s = 0
    for i in range(1,len(l),2):
        s+=l[i]
    return s

n = int(input())
nums = list(map(int,input().split()))
print(oddpossum(nums))