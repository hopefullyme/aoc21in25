from utils.reading import read_csv
from statistics import median

def solve():
    # inputs = read_csv('inputs/test7.txt')
    inputs = read_csv('inputs/7.txt')
    crab_min = min(inputs)
    crab_max = max(inputs)
    costs = []
    for target in range(crab_min, crab_max):
        fuel_cost = 0
        for crab in inputs:
            fuel_cost += crab_move_cost(crab, target)
        
        # Move to {target} costs {fuel_cost}
        costs.append((target, fuel_cost))
    

    least_cost = min(costs, key=lambda x: x[1])
    print(least_cost)
    

def crab_move_cost(init, target):
    return sum(range(abs(target - init)+1))