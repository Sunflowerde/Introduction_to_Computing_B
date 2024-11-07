import math

n=int(input())

for _ in range(n):
    a,b,c=map(float,input().split())
    
    number="{:.5f}".format(-b/(2*a))
    
    if b*b-4*a*c>0:
        x10="{:.5f}".format((-b+math.sqrt(b*b-4*a*c))/(2*a))
        x20="{:.5f}".format((-b-math.sqrt(b*b-4*a*c))/(2*a))
        print(f"x1={x10};x2={x20}")
    elif b*b-4*a*c==0:
        print(f"x1=x2={x10}")
    elif b*b-4*a*c<0:
        y1="{:.5f}".format((math.sqrt(4*a*c-b*b))/(2*a))
        x11=str(number)+"+"+str(y1)+"i"
        x21=str(number)+"-"+str(y1)+"i"
        
        
        print(f"x1={x11};x2={x21}")