import math
t=int(input())
for _ in range(t):
    n=int(input())
    print(n*(n+1)//2-2*(pow(2,int(math.log(n,2))+1)-1))