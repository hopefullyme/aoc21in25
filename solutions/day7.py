from utils.reading import read_csv
from statistics import median

def solve():
    # inputs = read_csv('inputs/test7.txt')
    # inputs = read_csv('inputs/7.txt')
    # t_pos = median(inputs)
    # fuel_cost = 0
    # for crab in inputs:
    #     fuel_cost += abs(crab - t_pos)
    answer = crab_move_cost(16, 5)
    print(answer)
    assert(answer == 66)
    

def crab_move_cost(init, target):
    return sum(range(abs(target - init)+1))