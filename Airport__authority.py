n = int(input())
weights = []
for i in range(n):
    weights.append(int(input()))
t = int(input())
cost = 0

for i in range(n):
    if weights[i] <= t:
        cost+=1
    else:
        cost+=2
print(cost)