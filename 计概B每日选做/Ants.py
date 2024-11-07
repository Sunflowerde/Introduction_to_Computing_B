t=int(input())
for _ in range(t):
    a=[]
    b=[]
    l,n=map(int,input().split())
    x=list(map(int,input().split()))
    for i in x:
        a.append(min(i,l-i))
        b.append(max(i,l-i))
    print(max(a),max(b))