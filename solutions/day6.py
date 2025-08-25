from utils.reading import read_csv
from multiprocessing.pool import Pool
from itertools import chain
from time import perf_counter

def solve():
    lanternfish = read_csv("inputs/6.txt")
    print(lanternfish)
    lf_counts = count_fish(lanternfish)
    print(lf_counts)
    for _ in range(256):
        lf_next = [0] * 9
        for age, fishes in enumerate(lf_counts):
            if age == 0:
                lf_next[6] += fishes
                lf_next[8] += fishes
            else:
                lf_next[age - 1] += fishes
        lf_counts = lf_next
            
    print(sum(lf_counts))

def count_fish(fishes):
    result = [0] * 9
    for f in fishes:
        result[f] += 1
    return result