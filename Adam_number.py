n = int(input())
m = int(str(n)[::-1])
print(True if str(m**2)[::-1] == str(n**2) else False)