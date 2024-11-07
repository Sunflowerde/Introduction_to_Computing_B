while True:
    n,m=map(int,input().split())
    if n+m==0:
        break
    a=0
    for i in range(2,n+1):
        a=(a+m)%i
    print(a+1)