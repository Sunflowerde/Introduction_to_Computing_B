case_number=1

while True:
    p,e,i,d=map(int,input().split())
    
    if p==-1:
        break
    
    for j in range(d+1,d+21253):
        if (j-p)%23==0 and (j-e)%28==0 and (j-i)%33==0:
            print(f"Case {case_number}: the next triple peak occurs in {j-d} days.")
            break
            
    case_number+=1