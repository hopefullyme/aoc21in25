from utils.reading import file_to_list_of_lines
def solve():
    # input = file_to_list_of_lines('inputs/3.txt')
    input = file_to_list_of_lines('inputs/test3.txt')

    bitsInPos = [[bitstr[i] for bitstr in input] for i in range(len(input[0]))]
    # print(bitsInPos)
    # gamma = getGamma(bitsInPos)
    # print(gamma)
    # epsilon = getEpsilon(bitsInPos)

    # oxygen generator rating
    ogr = getOxyRate(input)
    print(int(ogr, 2))

def getGamma(bitLists):
    # most common bit from each position
    gamma = ''
    for bitlist in bitLists:
        counts = countBits(bitlist)
        if counts[0] > counts[1]:
            gamma += '0'
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

def getOxyRate(input):
    numList = input.copy()
    # for each pos:
    for pos in range(len(numList[0])):
        nextList = []
        #  find the most common bit (if counts are even, use 1)
        mcBit = getMostCommonBit(pos, numList)
        #  keep only the ones with that bit in that pos
        for num in numList:
            if hasBitInPos(num, mcBit, pos):
                nextList.append(num)
        numList = nextList
    return numList[0]    

def hasBitInPos(str, bit, pos):
    return str[pos] == bit

def getMostCommonBit(pos, numList):
    zeroes = 0
    ones = 0
    for num in numList:
        if num[pos] == '1':
            ones += 1
        else:
            zeroes += 1
    if ones >= zeroes:
        return '1'
    else:
        return '0'
    
def countBits(bitStr):
    zeroes = bitStr.count('0')
    ones = bitStr.count('1')
    return (zeroes, ones)