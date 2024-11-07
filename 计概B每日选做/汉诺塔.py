def move(n,start,mid,end):
    if n==0:
        return
    move(n-1,start,end,mid)
    print(f"{start}->{end}")
    move(n-1,mid,start,end)
    
n=int(input())
print(2**n-1)
move(n,"A","B","C")