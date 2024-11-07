n,k=map(int,input().split())
lst=list(map(int,input().split()))

left=0
right=len(lst)-1
cnt=0

while left<right:
    if lst[left]+lst[right]>k:
        right-=1
    elif lst[left]+lst[right]==k:
        left+=1
        right-=1
        cnt+=1
    else:
        left+=1
        
print(cnt)