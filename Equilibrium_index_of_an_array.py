for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    ind = -1
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            ind = i
            break
    print(ind)