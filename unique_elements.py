n = int(input())
l = list(map(int,input().split()))
unq = []
for i in l:
    if i not in unq:
        unq.append(i)
print(*unq)
