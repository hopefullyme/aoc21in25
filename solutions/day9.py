from utils.reading import file_to_list_of_lines
from collections import deque

def solve():
    inputs = file_to_list_of_lines('inputs/9.txt')
    grid_str = [list(line) for line in inputs]
    grid = [[int(h) for h in row] for row in grid_str]
    points = get_low_points(grid)
    basins = [get_basin(point, grid) for point in points]
    b = sorted(basins)
    
    answer = b[-1] * b[-2] * b[-3]
    print(answer)

def get_low_points(grid):
    points = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            height = grid[y][x]
            neighbors = []
            if y > 0:
                neighbors.append(grid[y-1][x])
            if x > 0:
                neighbors.append(grid[y][x-1])
            if y < len(grid) - 1:
                neighbors.append(grid[y+1][x])
            if x < len(grid[y]) - 1:
                neighbors.append(grid[y][x+1])
            
            if height < min(neighbors):
                points.append((y, x))
    return points

def get_basin(start, grid):
    basin = bfs(grid, start)
    return len(basin)

def bfs(grid, point):
    height = grid[point[0]][point[1]]
    q = deque([point])
    visited = [point]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]    

    while q:
        y,x = q.popleft()
        height = grid[y][x]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            # check we're not revisiting points
            if (ny, nx) in visited:
                continue
            # check edges and height
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] >= height and grid[ny][nx] != 9:
                q.append((ny, nx))
                visited.append((ny, nx))
    return visited