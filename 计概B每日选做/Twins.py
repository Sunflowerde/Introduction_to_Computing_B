n=int(input())
lst=sorted(list(map(int,input().split())),reverse=True)
total=sum(lst)

tmp=0
i=0
while tmp<=total-tmp:
    tmp+=lst[i]
    i+=1
print(i)