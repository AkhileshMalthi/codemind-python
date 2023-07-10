# Akhilesh Malthi
# Input = a list of numbers.
# output = a sorted list of numbers which satisfies the condition.
# condition = sum of factors of the number in the given list, is present in the list.
def SumofFactors(n):
    li = [i for i in range(1,n+1) if n%i==0]
    return sum(li)
    
ol = list(map(int,input().split(",")))
result = [i for i in ol if SumofFactors(i) in ol]
if result == []:
    print(-1)
else:
    print(*sorted(result))
