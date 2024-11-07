n,k=map(int,input().split())
a=[]
if k<=10:
    while n!=0:
        a.append(str(n%k))
        n=n//k
else:
    b=["A","B","C","D","E","F"]
    while n!=0:
        if n%k<10:
            a.append(str(n%k))
        else:
            a.append(b[n%k-10])
        n=n//k
a.reverse()
print("".join(a))