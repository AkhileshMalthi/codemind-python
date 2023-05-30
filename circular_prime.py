def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True


n = input()
if isprime(int(n)) and isprime(int(n[::-1])):
    print("circular prime")
elif isprime(int(n)):
    print("prime but not a circular prime")
else:
    print("not prime")