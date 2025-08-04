from utils.reading import file_to_list_of_lines
def solve():
    input = file_to_list_of_lines('inputs/3.txt')
    # input = file_to_list_of_lines('inputs/test3.txt')

    bitsInPos = [[bitstr[i] for bitstr in input] for i in range(len(input[0]))]
    # print(bitsInPos)
    gamma = getGamma(bitsInPos)
    print(gamma)
    epsilon = getEpsilon(bitsInPos)
    print(epsilon)

    print("\n")
    print(gamma * epsilon)

def getGamma(bitLists):
    # most common bit from each position
    gamma = ''
    for bitlist in bitLists:
        counts = countBits(bitlist)
        if counts[0] > counts[1]:
            gamma += '0'
        else:
            gamma += '1'
    gDec = int(gamma, 2)
    return gDec
    
def getEpsilon(bitLists):
    # least common bit from each position
    ep = ''
    for bitlist in bitLists:
        counts = countBits(bitlist)
        if counts[0] < counts[1]:
            ep += '0'
        else:
            ep += '1'
    epDec = int(ep, 2)
    return epDec

def countBits(bitList):
    zeroes = bitList.count('0')
    ones = bitList.count('1')
    return (zeroes, ones)