n=int(input())
lst=list(map(int,input().split()))
tmp=0

count=[0]*5
for i in lst:
    count[i]+=1
    
tmp+=count[4]

tmp+=count[3]
count[1]=max(0,count[1]-count[3])

tmp+=count[2]//2
if count[2]%2==1:
    tmp+=1
    count[1]=max(0,count[1]-2)
    
tmp+=count[1]//4
if count[1]%4!=0:
    tmp+=1
    
print(tmp)
