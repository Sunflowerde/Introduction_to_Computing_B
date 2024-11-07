import math

def screen(n,prime):
    for i in range(4,n+1,2):
        prime[i]=False
    p=3
    while p*p<=n:
        if prime[p]==True:
            for i in range(2*p,n+1,p):
                prime[i]=False
        p+=2
    return prime

n=input()
lst=list(map(int,input().split()))
s=[True]*(10**6+1)
prime=screen(10**6,s)

for i in lst:
    if i<4:
        print("NO")
        continue
    if math.isqrt(i)**2!=i:
        print("NO")
        continue
    if prime[math.isqrt(i)]:
        print("YES")
    else:
        print("NO")