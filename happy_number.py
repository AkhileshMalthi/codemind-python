def sqsum(n):
    ss = 0
    for i in range(len(n)):
      ss += int(n[i])**2
    return ss
n = input()
n = sqsum(n)
while n>9:
    n = sqsum(str(n))
print(True if n==1 or n==7 else False)
