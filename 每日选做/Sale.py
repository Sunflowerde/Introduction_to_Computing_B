n,m=map(int,input().split())
lst=sorted(list(map(int,input().split())))
money=[]

for i in lst[:m]:
    if i<=0:
        money.append(abs(i))

print(sum(money))