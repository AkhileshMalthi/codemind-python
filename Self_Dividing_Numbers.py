def selfdividing(n):
    for i in range(len(n)):
        if n[i]=="0" or int(n)%int(n[i])!=0:
            return False
    return True

a=int(input())
b=int(input())
for i in range(a,b+1):
    if selfdividing(str(i)):
        print(i,end=" ")
