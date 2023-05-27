def ispalin(n):
    return True if str(n)[::-1] == str(n) else False

n = int(input())
i = 1
while True:
    if ispalin(n+i) and ispalin(n-i):
        print(n-i,n+i)
        break
    elif ispalin(n+i):
        print(n+i)
        break
    elif ispalin(n-i):
        print(n-i)
        break
    i+=1
