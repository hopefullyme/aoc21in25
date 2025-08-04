import os.path

def file_to_list_of_lines(filename):
    if not os.path.isfile(filename):
        print(f"Error: no file with name {filename}")
    else: 
        with open(filename) as f:
            return f.read().splitlines()

def file_to_numbers(filename):
    lines = file_to_list_of_lines(filename)
    result = [int(a) for a in lines]
    return result

def testAvailable():
    print("Reading module available")

