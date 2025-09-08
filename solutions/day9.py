from utils.reading import file_to_list_of_lines

def solve():
    inputs = file_to_list_of_lines('inputs/test9.txt')
    grid_str = [list(line) for line in inputs]
    grid = [[int(h) for h in row] for row in grid_str]
    print(grid)