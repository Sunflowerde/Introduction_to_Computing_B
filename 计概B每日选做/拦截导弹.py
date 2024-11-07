k=int(input())
h=list(map(int,input().split()))
dp=[1]*k

for i in range(k):
    for j in range(i):
        if h[i]<=h[j]:
            dp[i]=max(dp[i],dp[j]+1)
            
print(max(dp))