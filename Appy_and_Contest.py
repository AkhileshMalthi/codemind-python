tc = int(input())
for t in range(tc):
   n,a,b,k = map(int,input().split())
   s = 0
   for i in range(1,n+1):
       if i%a==0 and i%b!=0:
           s+=1
       elif i%a!=0 and i%b==0:
           s+=1
       if s>=k:
           print("Win")
           break
   else:
        print("Lose")