import utils.reading as r

def solve():
    in_data = r.file_to_list_of_lines('inputs/1.txt')
    data = [int(x) for x in in_data]
    windows = []
    depth_increases = 0
    
    for i in range(2, len(data)):
        windows.append(data[i]+data[i-1]+data[i-2])
    
    for j in range(1, len(windows)):
        if windows[j] > windows[j-1]:
            depth_increases += 1

    print(depth_increases)
