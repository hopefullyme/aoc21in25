import utils.reading as r

def solve():
    data = r.file_to_list_of_lines('inputs/1.txt')
    depth_increases = 0
    for i in range(1, len(data)):
        if int(data[i]) > int(data[i-1]):
            depth_increases += 1
    
    print(depth_increases)