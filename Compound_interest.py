import math
p,r,t = map(float,input().split())
result = p*pow(1+r/100,t)
print("%.2f" % result)