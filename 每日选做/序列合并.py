n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=sorted(a+b)
print(*c)