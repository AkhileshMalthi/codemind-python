n = input()
m = str(int(n)*int(n))
if m[len(m)-len(n):] == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    