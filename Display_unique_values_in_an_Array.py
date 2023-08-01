# Algorithm:
#     1. Take each value in the list
#     2. Print the value whose count in the list is 1

n = int(input())
nums = list(map(int,input().split()))
nouniques = True
for eachnum in nums:
    if nums.count(eachnum) == 1:
        nouniques = False
        print(eachnum,end=" ")
if nouniques:
    print(-1)
