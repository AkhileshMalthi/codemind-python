n = int(input())
nums = list(map(int,input().split()))
for i in nums:
    if i%2!=0:
        print(False)
        break
else:
    print(True)