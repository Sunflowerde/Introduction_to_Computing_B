def permutation(lst):
    
    length=len(lst)
    i=length-2
    
    while i>=0 and lst[i]>lst[i+1]:
        i-=1
        if i>=0:
            j=length-1
            while j>=0 and lst[i]>=lst[j]:
                j-=1
            lst[i],lst[j]=lst[j],lst[i]
            
    left=i+1
    right=length-1
    while left<right:
        lst[left],lst[right]=lst[right],lst[left]
        left+=1
        right-=1
        
m=int(input())
for _ in range(m):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    for _ in range(k):
        permutation(lst)
    
    print(*lst)