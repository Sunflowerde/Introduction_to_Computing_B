t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    prefix_sum=0
    prefix_sums=set()
    cnt=0
    
    for i in a:
        prefix_sum+=i
        if prefix_sum==0 or prefix_sum in prefix_sums:
            cnt+=1
            prefix_sum=0
            prefix_sums.clear()
        else:
            prefix_sums.add(prefix_sum)
            
    print(cnt)