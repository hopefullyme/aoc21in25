from utils.reading import read_csv
from statistics import median

def solve():
    # inputs = read_csv('inputs/test7.txt')
    inputs = read_csv('inputs/7.txt')
    t_pos = median(inputs)
    fuel_cost = 0
    for crab in inputs:
        fuel_cost += abs(crab - t_pos)
    print(fuel_cost)
    