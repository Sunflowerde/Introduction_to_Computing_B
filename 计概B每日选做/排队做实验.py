n=int(input())
lst=list(map(int,input().split()))

index_lst=[(index+1,value) for index,value in enumerate(lst)]
sorted_lst=sorted(index_lst,key=lambda x:x[1])
sorted_index=[str(index) for index,value in sorted_lst]

print(" ".join(sorted_index))

total=0
for i in range(n-1,0,-1):
    total+=i*sorted_lst[n-1-i][1]

print("{:.2f}".format(total/n))