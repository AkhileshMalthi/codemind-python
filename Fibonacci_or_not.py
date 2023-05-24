def isfib(n):
    a = 0
    b = 1
    while a<=n:
        if a == n:
            return True
        c=a+b
        a=b
        b=c
    else:
        return False
        
n = int(input())
print(True if n==1 or n==0 else isfib(n))
