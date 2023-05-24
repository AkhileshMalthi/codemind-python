n = int(input())
factors = [x for x in range(2,(n//2)+1) if n%x==0]
print(True if sum(factors)>n else False)