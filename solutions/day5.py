from utils.reading import file_to_list_of_lines
import re

def solve():
    puz_input = file_to_list_of_lines('inputs/test5.txt')
    # puz_input = file_to_list_of_lines('inputs/5.txt')
    coords = parse_input(puz_input)
    seafloor_map = map_coords(coords)
    

def parse_input(input):
    myregx = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    matches = [myregx.match(ln).group(1,2,3,4) for ln in input]
    coords = [[int(val) for val in st] for st in matches]
    return coords

def map_coords(coords):
    (xsize, ysize) = map_size(coords)
    da_map = [[0 for _ in range(ysize+1)] for _ in range(xsize+1)]
    print(da_map)
    for (x1, y1, x2, y2) in coords:
        if x1 == x2 or y1 == y2:
            pass

def map_size(coords):
    maxX = 0
    maxY = 0
    for (x1, y1, x2, y2) in coords:
        if x1 > maxX:
            maxX = x1
        if x2 > maxX:
            maxX = x2
        if y1 > maxY:
            maxY = y1
        if y2 > maxY:
            maxY = y2
    return (maxX, maxY)