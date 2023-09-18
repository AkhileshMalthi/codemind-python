n = int(input())
for i,num in enumerate(list(map(int,input().split()))):
    if num%2==0 and i%2!=0:
        print(False)
        break
else:
    print(True)