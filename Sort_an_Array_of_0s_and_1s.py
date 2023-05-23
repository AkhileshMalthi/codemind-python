n = int(input())
li = list(map(str,input().split()))
nli = [x for x in li if x == "0"]
nli.extend(x for x in li if x == "1")
print(*nli)