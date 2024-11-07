n=int(input())
x=sorted(list(map(int,input().split())))
waiting_time=0
satisfied_people=0
for time in x:
    if waiting_time<=time:
        waiting_time+=time
        satisfied_people+=1
print(satisfied_people)