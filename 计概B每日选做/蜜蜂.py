n=int(input())

dp=[0]*101
dp[1],dp[2]=1,1
for i in range(3,101):
    dp[i]=dp[i-1]+dp[i-2]

for _ in range(n):
    a,b=map(int,input().split())
    print(dp[1+b-a])