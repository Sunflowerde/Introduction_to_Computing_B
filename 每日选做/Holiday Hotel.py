N=int(input())
distance_cost={}
for _ in range(N):
    D,C=map(int,input().split())
    distance_cost[D]=C
n=int(input())
cost_distance={cost:distance for distance,cost in distance_cost}
most_value=0
distance_list=[]
cost_list=[]
min_distance=min(distance_cost.keys())
min_cost=min(distance_cost.values())
distance_list.append(distance_cost[min_distance])
cost_list.append(cost_distance[min_cost])
most_value=cost_list.count(min(cost_list))+distance_list.count(min(distance_list))
print(most_value)