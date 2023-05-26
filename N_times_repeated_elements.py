n = int(input())
l = list(map(int,input().split()))
k = int(input())
unq = []
kreps = []
for i in l:
    if i not in unq:
        unq.append(i)
for i in unq:
    if l.count(i) == k:
        kreps.append(i)
if len(kreps) == 0:
    print(-1)
else :
    print(*kreps)