p=int(input())
lst=sorted(list(map(int,input().split())))

left=0
right=len(lst)-1
cnt=0

while left<=right:
    
    if p>=lst[left]:
        p-=lst[left]
        cnt+=1
        left+=1
        
    else:
        if left==right:
            break
        
        p+=lst[right]
        cnt-=1
        
        if cnt<0:
            cnt=0
            break
            
        right-=1
        
print(cnt)