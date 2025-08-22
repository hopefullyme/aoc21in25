from utils.reading import read_csv
from multiprocessing.pool import Pool
from itertools import chain
from time import perf_counter

def solve():
    lanternfish = read_csv("inputs/6.txt")
    print(lanternfish)
    for i in range(80):
        lf_next = []
        for f in lanternfish:
            if f == 0:
                lf_next.extend([6, 8])
            else:
                lf_next.append(f - 1)
        print(f"day {i} - {len(lf_next)} fish")
        lanternfish = lf_next
            
    print(len(lanternfish))
