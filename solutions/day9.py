from utils.reading import file_to_list_of_lines

def solve():
    inputs = file_to_list_of_lines('inputs/9.txt')
    grid_str = [list(line) for line in inputs]
    grid = [[int(h) for h in row] for row in grid_str]
    points = get_low_points(grid)
    risk_levels = [h+1 for h in points]
    print(sum(risk_levels))

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
                points.append(height)
    return points