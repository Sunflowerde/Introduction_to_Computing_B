n,w=map(int,input().split())
a=[]
for _ in range(n):
    p,q=map(int,input().split())
    for _ in range(q):
        a.append(p/q)
a.sort(reverse=True)
x=sum(a[:w])
print("{:.1f}".format(x))