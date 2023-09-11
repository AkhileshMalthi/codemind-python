n = int(input())
nums = list(map(int,input().split()))[::-1]
dec = 0
for i in range(n):
    dec += nums[i]*2**i
print(dec)