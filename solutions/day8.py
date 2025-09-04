from utils.reading import file_to_list_of_lines

def solve():
    input = file_to_list_of_lines('inputs/test8.txt')
    entries = tokenize(input)
    sig_sorted_entries = map(sort_signals, entries)
    for entry in sig_sorted_entries:
        legend = analyze(entry)
        print(legend)
        

def tokenize(lines):
    return map(lambda l: l.split(), lines)

def sort_signals(entry):
    # "abcd" needs to be treated the same as "dcba" so we sort each signal collection
    return [''.join(sorted(dig)) for dig in entry if dig != '|']

def output_values(entry):
    return entry[-4:]

def count_segs(entry):
    # turns e.g. [fdgacbe, cefdb, cefbgd, gcbe] into [7, 5, 6, 4]
    # by counting the letters ("illuminated segments") in each string ("digit")
    return map(len, entry)

def analyze(line):
    # returns dict: "legend" which maps the garbled outputs to intended outputs s.t. 
    # if w (a-g) is the wire turning on, legend[w] (A-G) is the segment that's supposed to illuminate (0 means we don't know yet)
    legend = {'a': 0, 'b': 0, 'c':0, 'd': 0, 'e': 0, 'f': 0, 'g':0}

    # strs[n] is the string that means the display is trying to show digit n (if we know)
    strs = [''] * 10
    # count how many times each wire lights up while displaying each digit once
    times_illuminated = {'a': 0, 'b': 0, 'c':0, 'd': 0, 'e': 0, 'f': 0, 'g':0}

    for digit in line[:-4]:
        for w in digit:
            times_illuminated[w] += 1
        # unique-length digits
        if len(digit) == 2:
            strs[1] = digit
        elif len(digit) == 4:
            strs[4] = digit
        elif len(digit) == 3:
            strs[7] = digit
        elif len(digit) == 7:
            strs[8] = digit
    
    # We Know: 
    # the segment that lights up 4 times is 4/e
    # the segment that lights up 6 times is 1/b
    # the segment that lights up 9 times is 5/f

    for (wire, times) in times_illuminated.items():
        if times == 4:
            legend[wire] = 'E'
        if times == 6:
            legend[wire] = 'B'
        if times == 9:
            legend[wire] = 'F'

        # One that lights up 8 times is either 0/a or 2/c
        # Differentiate between A and C by: C appears in strs[1] and A doesn't
        if times == 8:
            if wire in strs[1]:
                legend[wire] = 'C'
            else:
                legend[wire] = 'A'
        
        # One that lights up 7 times is either 3/d or 6/g
        # Differentiate between D and G by: D appears in strs[4] and G doesn't
        if times == 7:
            if wire in strs[4]:
                legend[wire] = 'D'
            else:
                legend[wire] = 'G'

    return legend
