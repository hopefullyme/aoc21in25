from utils.reading import file_to_list_of_lines
import re
def solve():
    directions = file_to_list_of_lines("inputs/2.txt")
    horizontal_pos = 0
    depth = 0
    aim = 0
    for i in range(len(directions)):
        instruction = re.match(r'(forward|up|down) (\d+)', directions[i])
        dir = instruction.group(1)
        amount = int(instruction.group(2))
        if dir == 'forward':
            horizontal_pos += amount
            depth += aim * amount
        elif dir == "down":
            aim += amount
        elif dir == "up":
            aim -= amount
        else:
            print("Something is very wrong")
    
    print(horizontal_pos)
    print(depth)
    print(horizontal_pos * depth)