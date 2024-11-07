n=int(input())
x=[0]*21
x[1]=x[2]=1
for i in range(3,21):
    x[i]=x[i-1]+x[i-2]
for _ in range(n):
    a=int(input())
    print(x[a])