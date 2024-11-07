n=int(input())
trees=[]
last_position=-float("inf")
cnt=0

for i in range(n):
    x,h=map(int,input().split())
    trees.append([x,h])
    
for i in range(n):
    if trees[i][0]-trees[i][1]>last_position:
        cnt+=1
        last_position=trees[i][0]
        
    elif i==n-1 or trees[i][0]+trees[i][1]<trees[i+1][0]:
        cnt+=1
        last_position=trees[i][0]+trees[i][1]
        
    else:
        last_position=trees[i][0]
        
print(cnt)