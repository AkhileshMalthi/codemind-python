def isodd(n):
    return True if n%2!=0 else False

n = int(input())
nums = list(map(int,input().split()))
odds = list(filter(isodd,nums))
print(sum(odds))