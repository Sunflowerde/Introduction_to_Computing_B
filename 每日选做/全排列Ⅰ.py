import itertools
n=int(input())
lst=list(range(1,n+1))
permutations=itertools.permutations(lst)
for i in permutations:
    print(" ".join(map(str,i)))