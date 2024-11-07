t=int(input())

for _ in range(t):
    n=int(input())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    
    sum1=min(lst1)*n+sum(lst2)
    sum2=min(lst2)*n+sum(lst1)
    
    print(min(sum1,sum2))