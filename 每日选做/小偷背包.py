N,B=map(int,input().split())
price=list(map(int,input().split()))
weight=list(map(int,input().split()))

dp=[[0]*(B+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,B+1):
        if weight[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],price[i-1]+dp[i-1][j-weight[i-1]])
            
print(dp[N][B])