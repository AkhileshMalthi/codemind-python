n  = input()
l = []
for i in range(len(n)):
    l.append(int(n[i])**(i+1))
print(True if sum(l)==int(n) else False)