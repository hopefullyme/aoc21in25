from utils.reading import file_to_list_of_lines

def solve():
    input = file_to_list_of_lines('inputs/8.txt')
    entries = tokenize(input)
    outputs_only = map(output_values, entries)
    illuminated_segments = map(count_segs, outputs_only)
    
    # count how many patterns are each length
    counts = [0] * 10
    for line in illuminated_segments:
        for digit in line:
            counts[digit] += 1
    
    # for part one we want to know how many (1, 4, 7, 8)'s there are
    # which corresponds to digits of length (2, 4, 3, 7)
    p1_ans = sum((counts[2], counts[4], counts[3], counts[7]))

    
    print(p1_ans)

def tokenize(lines):
    return map(lambda l: l.split(), lines)

def output_values(entry):
    return entry[-4:]

def count_segs(entry):
    # turns e.g. [fdgacbe, cefdb, cefbgd, gcbe] into [7, 5, 6, 4]
    # by counting the letters ("illuminated segments") in each string ("digit")
    return map(len, entry)