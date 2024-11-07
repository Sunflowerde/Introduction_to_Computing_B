import math

t=int(input())
for _ in range(t):
    x,y,k=map(int,input().split())
    if math.ceil(y/k)>=math.ceil(x/k):
        print(2*math.ceil(y/k))
    else:
        print(2*math.ceil(x/k)-1)