from utils.reading import file_to_list_of_lines

def solve():
    input = file_to_list_of_lines('inputs/test8.txt')
    entries = tokenize(input)
    print(entries[0])

def tokenize(lines):
    return list(map(lambda l: l.split(), lines))
