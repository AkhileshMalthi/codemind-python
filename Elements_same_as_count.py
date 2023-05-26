n = int(input())
l = list(map(int,input().split()))
unq = []
sameascount = []
for i in l:
    if i not in unq:
        unq.append(i)
for i in unq:
    if l.count(i) == i:
        sameascount.append(i)
if len(sameascount) == 0:
    print(-1)
else :
    print(*sameascount)