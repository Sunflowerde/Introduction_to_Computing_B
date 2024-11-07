m=int(input())

dp=[0]*27
dp[1],dp[2]=1,2
for i in range(3,27):
    dp[i]=dp[i-1]+dp[i-2]+i

for _ in range(m):
    n=int(input())
    print(dp[n])