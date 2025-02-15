cost = [1,2,1,2,1,1,1]

length = len(cost)

cost.append("Final")

def climb(cost):
    min_cost = 0
    min_2_cost = 0
    for i in range(length):
        if (min_cost + cost[i]) < (min_cost+ cost[i+1]):
            min_cost += cost[i]
        else:
            min_cost += cost[i+1]
            i += 1
    
    for i in range(1,length):
        if (min_2_cost + cost[i]) < (min_2_cost+ cost[i+1]):
            min_2_cost += cost[i]
        else:
            min_2_cost += cost[i+1]
            i += 1
    
    if min_cost < min_2_cost:
        return min_cost
    else:
        return min_2_cost+50000

some = climb(cost)

print(some)