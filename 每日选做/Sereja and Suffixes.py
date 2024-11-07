n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for _ in range(m):
    li=int(input())
    l.append(li)
    
dp=[0]*(n+3)
sets=set()
for i in range(n,0,-1):
    if a[i-1] not in sets:
        sets.add(a[i-1])
        dp[i]=len(sets)
        
    else:
        dp[i]=dp[i+1]
        
results=[]
for i in range(m):
    results.append(dp[l[i]])
    
print("\n".join(map(str,results)))