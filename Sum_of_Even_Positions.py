def evenpossum(l):
    s = 0
    for i in range(0,len(l),2):
        s+=l[i]
    return s

n = int(input())
nums = list(map(int,input().split()))
print(evenpossum(nums))