n=input()
while len(n)>1:
    total=0
    for i in range(len(n)):
        total+=int(n[i])
    n=str(total)
print(n)