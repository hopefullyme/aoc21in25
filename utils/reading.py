import os.path

def file_to_list_of_lines(filename):
    if not os.path.isfile(filename):
        print(f"Error: no file with name {filename}")
    else: 
        with open(filename) as f:
            return f.read().splitlines()
        
def testAvailable():
    print("Reading module available")