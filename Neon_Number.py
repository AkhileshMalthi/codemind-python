def SUM(n):
    l=[int(n[x]) for x in range(len(n))]
    return sum(l)
    
n=int(input())
m=n**2
while m>9:
    m = SUM(str(m))
if m==n:
    print("Neon Number")
else:
    print("Not Neon Number")
