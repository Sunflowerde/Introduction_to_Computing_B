n=int(input())
lst=list(map(int,input().split()))

if lst==sorted(lst):
    print("YES")
else:
    print("NO")