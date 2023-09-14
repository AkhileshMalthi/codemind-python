def BinaryArrorNot(nums):
    for i in nums:
        if i == 0 or i == 1:
            continue
        else:
            return False
    return True

n = int(input())
nums = list(map(int,input().split()))
print(BinaryArrorNot(nums))