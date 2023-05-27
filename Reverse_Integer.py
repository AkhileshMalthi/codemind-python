n = int(input())
if n > 0:
    print(int(str(n)[::-1]))
else:
    print(-1*int(str(abs(n))[::-1]))