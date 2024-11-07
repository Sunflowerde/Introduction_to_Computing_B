n=int(input())

dp=[0]*27
dp[1],dp[2]=1,2

for i in range(3,27):
    dp[i]=dp[i-1]+2*dp[i-2]
    
print(dp[n])