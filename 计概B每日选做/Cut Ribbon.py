n,a,b,c=map(int,input().split())
dp=[-float("inf")]*(n+1)
dp[0]=0 #dp[i]表示长度为i时的最大切割数

for i in range(1,n+1):
    if i>=a:
        dp[i]=max(dp[i],dp[i-a]+1)
    if i>=b:
        dp[i]=max(dp[i],dp[i-b]+1)
    if i>=c:
        dp[i]=max(dp[i],dp[i-c]+1)
        
print(dp[n])