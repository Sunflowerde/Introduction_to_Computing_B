import math
decomposition=[]
n=int(input())
while n%2==0:
    decomposition.append(2)
    n=n//2
for i in range(3,int(math.sqrt(n))+1,2):
    while n%i==0:
        decomposition.append(i)
        n=n//i
if n>2:
    decomposition.append(n)
if len(decomposition)!=len(set(decomposition)):
    print(0)
elif len(decomposition)%2!=0:
    print(-1)
elif len(decomposition)%2==0:
    print(1)