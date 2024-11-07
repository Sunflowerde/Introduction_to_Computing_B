n,q=map(int,input().split())
likes=[]
for _ in range(q):
    x,y=map(int,input().split())
    likes.append([x,y])
found=False
for i in range(q):
    for j in range(q):
        for k in range(q):
            if likes[i][1]==likes[j][0] and likes[j][1]==likes[k][0] and likes[k][1]==likes[i][0]:
                found=True
            if found:
                break
if found:
    print("Yes")
else:
    print("No")