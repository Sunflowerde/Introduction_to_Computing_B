def solve(position,x1,x2,y1,y2):
    n=len(position)
    for i in range(n):
        if (position[i][0]-x2)**2+(position[i][1]-y2)**2<=(x1-x2)**2+(y1-y2)**2:
            return "no"
    return "yes"

t=int(input())
for _ in range(t):
    n=int(input())
    position=[]
    for _ in range(n):
        x,y=map(int,input().split())
        position.append((x,y))
    x1,y1,x2,y2=map(int,input().split())
    print(solve(position,x1,x2,y1,y2))