n=int(input())
weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
mod=["1","0","X","9","8","7","6","5","4","3","2"]
for _ in range(n):
    total=0
    s=input()
    for i in range(17):
        total+=int(s[i])*weight[i]
    x=total%11
    if mod[x]!=s[17]:
        print("NO")
    else:
        print("YES")