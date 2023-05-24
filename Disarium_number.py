n = int(input())
m = list(map(int,str(n)))
s = 0
for i in range(1,len(m)+1):
    s += m[i-1]**i
print(True if s == n else False)