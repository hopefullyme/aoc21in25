from utils.reading import file_to_list_of_lines
def solve():
    # input = file_to_list_of_lines('inputs/3.txt')
    input = file_to_list_of_lines('inputs/test3.txt')

    bitsInPos = [[bitstr[i] for bitstr in input] for i in range(len(input[0]))]
    # print(bitsInPos)
    gamma = getGamma(bitsInPos)
    print(gamma)
    # epsilon = getEpsilon(bitsInPos)

    # oxygen generator rating
    ogr = getOxyRate(input, gamma)

def getGamma(bitLists):
    # most common bit from each position
    gamma = ''
    for bitlist in bitLists:
        counts = countBits(bitlist)
        print(counts)
        if counts[0] > counts[1]:
            gamma += '0'
        elif counts[0] == counts[1]:
            gamma += '-'
        else:
            gamma += '1'
    return gamma
    
def getEpsilon(bitLists):
    # least common bit from each position
    ep = ''
    for bitlist in bitLists:
        counts = countBits(bitlist)
        if counts[0] < counts[1]:
            ep += '0'
        elif counts[0] == counts[1]:
            ep += '-'
        else:
            ep += '1'
    return ep

def getOxyRate(nums, gamma):
    numList = nums.copy()
    # gamma has the most common bit for each bit positoin
    for pos, bit in enumerate(gamma):
        if bit == '-':
            bit = '1'
        nextList = []
        for num in numList:
            if hasBitInPos(num, bit, pos):
                nextList.append(num)
        numList = nextList
        print(numList)
    
        
    

def hasBitInPos(str, bit, pos):
    return str[pos] == bit

def countBits(bitList):
    zeroes = bitList.count('0')
    ones = bitList.count('1')
    return (zeroes, ones)