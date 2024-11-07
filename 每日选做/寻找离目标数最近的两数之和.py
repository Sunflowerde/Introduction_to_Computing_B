t=int(input())
s=list(map(int,input().split()))
s.sort()

left=0
right=len(s)-1
closest_sum=float("inf")

while left<right:
    current_sum=s[left]+s[right]
    
    if abs(current_sum-t)<abs(closest_sum-t):
        closest_sum=current_sum
    elif abs(current_sum-t)==abs(closest_sum-t):
        closest_sum=min(closest_sum,current_sum)
        
    if current_sum<t:
        left+=1
    else:
        right-=1
        
print(closest_sum)