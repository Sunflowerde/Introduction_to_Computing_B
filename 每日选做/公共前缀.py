n=int(input())
string=[]
for _ in range(n):
    s=input()
    string.append(s)
for i in range(n):
    for j in range(len(string[0])):
        if string[0][j]!=string[i][j]:
            sharing=string[0][:j]
            break
if sharing==None:
    print("")
else:
    print(sharing)