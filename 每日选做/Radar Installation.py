import math
test_number=1

def solve(n,d,position):
    ranges=[]
    cnt=1
    
    if d<0:
        return -1
    
    for x,y in position:
        if y>d:
            return -1
        delta=math.sqrt(d*d-y*y)
        ranges.append((x-delta,x+delta))
    
    if not ranges:
        return -1
    
    ranges=sorted(ranges,key=lambda x:x[1])
        
    loc=ranges[0][1]
    for start,end in ranges[1:]:
        if loc<start:
            loc=end
            cnt+=1
    return cnt

while True:
    position=[]
    n,d=map(int,input().split())
    if n==0 and d==0:
        break
    
    for _ in range(n):
        x,y=map(int,input().split())
        position.append((x,y))
    input()
    
    result=solve(n,d,position)
    
    print(f"Case {test_number}: {result}")
    test_number+=1