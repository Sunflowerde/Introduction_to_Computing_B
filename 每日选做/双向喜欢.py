n,q=map(int,input().split())
likes=[]
for _ in range(q):
    x,y=map(int,input().split())
    likes.append([x,y])
found=False
for i in range(q-1):
    for j in range(i+1,q):
        if likes[i][0]==likes[j][1] and likes[i][1]==likes[j][0]:
            found=True
        if found:
            break
if found:
    print("Yes")
else:
    print("No")