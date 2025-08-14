from utils.reading import file_to_list_of_lines
import re

def solve():
    # puz_input = file_to_list_of_lines('inputs/test5.txt')
    puz_input = file_to_list_of_lines('inputs/5.txt')
    coords = parse_input(puz_input)
    seafloor_map = map_coords(coords)
    overlaps = count_overlaps(seafloor_map)
    print(overlaps)

def parse_input(input):
    myregx = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    matches = [myregx.match(ln).group(1,2,3,4) for ln in input]
    coords = [[int(val) for val in st] for st in matches]
    return coords

def map_coords(coords):
    (xsize, ysize) = map_size(coords)
    da_map = [[0 for _ in range(ysize+1)] for _ in range(xsize+1)]
    for ptlist in coords:
        line = ends_to_pts(ptlist)
        # print(ptlist)
        # print(line)
        for pt in line:
            da_map[pt[0]][pt[1]] += 1
    return da_map 

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

def ends_to_pts(endpoints):
    (x1, y1, x2, y2) = endpoints
    xMin  = min(x1, x2)
    xMax = max(x1, x2)
    yMin = min(y1, y2)
    yMax = max(y1, y2)
    if x1 == x2:
        points = [(x1, y) for y in range(yMin, yMax+1)]
        return points
    if y1 == y2:
        points = [(x, y1) for x in range(xMin, xMax+1)]
        return points
    if x1 > x2:
        xs = range(x1, x2-1, -1)
    else:
        xs = range(x1, x2+1)
    if y1 > y2:
        ys = range(y1, y2-1, -1)
    else:
        ys = range(y1, y2+1)
    
    return list(zip(xs, ys))

def count_overlaps(sf_map):
    overlaps = 0
    ol_min = 2 
    for row in sf_map:
        for i in row:
            if i >= ol_min:
                overlaps += 1
    return overlaps