h=int(input())
m=int(input())
lst=[]
time=0
total=0

for _ in range(m):
    s,c=map(float,input().split())
    lst.append((s*c,s))
    
lst=sorted(lst,key=lambda x:x[0],reverse=True)
h0=2*h-0.5*m

for i in lst:
    if time>h0:
        break
    else:
        total+=i[0]*5/i[1]
        time+=5/i[1]
        
print("{:.1f}".format(total))