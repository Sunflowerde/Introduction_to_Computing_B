n=int(input())
lst=list(map(str,input().split()))

for i in range(n-1):
    for j in range(i+1,n):
        if lst[i]+lst[j]<lst[j]+lst[i]:
            lst[i],lst[j]=lst[j],lst[i]
            
max_number="".join(lst)
min_number="".join(reversed(lst))

print(max_number,min_number)