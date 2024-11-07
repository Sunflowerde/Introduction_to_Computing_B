from collections import Counter
def set_addition(lista,listb,sum):
    count=0
    dic1=Counter(lista)
    dic2=Counter(listb)
    for key in dic1:
        if sum-key in dic2:
            count+=dic1[key]*dic2[sum-key]
    return count 
n=int(input())
for _ in range(n):
    s=int(input()) 
    input()
    lista=list(map(int,input().split()))        
    input()
    listb=list(map(int,input().split()))
    print(set_addition(lista,listb,s))