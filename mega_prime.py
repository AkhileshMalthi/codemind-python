def isprime(n):
    if n==1: return False
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True

n = input()
if isprime(int(n)):
    for i in n:
        if isprime(int(i)) == False:
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")