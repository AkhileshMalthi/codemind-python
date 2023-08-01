# Algorithm:
#     1. Take all the unique Colour codes
#     2. Count each colour code in the list and
#     3. modulo by 2 and add the result to the number of pairs

n = int(input())
socks = list(map(int,input().split()))
codes = list(set(socks))
pairs = 0
for code in codes:
    pairs += socks.count(code)//2
print(pairs)