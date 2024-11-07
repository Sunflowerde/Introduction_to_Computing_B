def solve(n,k):
    dp=[[0]*(n+1) for _ in range(n+1)]
    dp[n][0]=1
    dp[n][n]=1
    dp[n][k]=dp[n-1][k-1]+dp[n-1][k]
    return dp[n][k]%(10**9+1)
    
t=int(input())
for _ in range(t):
    n=list(map(int,input().split()))
    k=list(map(int,input().split()))
    for i in range(len(n)):
        print(solve(n[i],k[i]))