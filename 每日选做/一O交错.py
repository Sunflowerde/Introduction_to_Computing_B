def solve(s):

    if s=="00" or s=="11":
        return 1
    if s=="10" or s=="01":
        return 2
        
    position1=0
    position2=0    
    for i in range(len(s)-2):
        if s[i]!=s[i+1]:
            position1=i
            break
    for j in range(position1,len(s)-2):
        if s[j]==s[j+1]:
            position2=j
            break
    return position2-position1+1

s=input()
print(solve(s))