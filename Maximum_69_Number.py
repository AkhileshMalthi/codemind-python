n = int(input())
m = str(n)
cl = []
cl.append(m)
for i in range(len(m)):
    if m[i] =="6":
        cl.append(m.replace("6","9",1))
    else:
        cl.append(m.replace("9","6",1))
cl = list(map(int,cl))
print(max(cl))