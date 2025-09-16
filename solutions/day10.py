from utils.reading import file_to_list_of_lines
from collections import deque
from statistics import median

SCORE_TABLE_SYNTAX = {
    ')' :3,
    ']': 57 ,
    '}': 1197 ,
    '>': 25137 
}

SCORE_TABLE_COMPLETION = {
    ')': 1 ,
    ']': 2 ,
    '}': 3 ,
    '>': 4 
}

def solve():
    input = file_to_list_of_lines("inputs/10.txt")
    scores = []
    for line in input:
        result = process_line(line)
        if result:
            scores.append( ac_score(result))
    print(median(scores))

def process_line(str):
    stack = deque()
    for ch in str:
        if ch in "({[<":
            stack.append(ch)
        elif ch in ")}]>":
            top = stack.pop()
            if (ch == ')' and top != '(') or \
                (ch == ']' and top != '[') or \
                (ch == '}' and top != '{') or \
                (ch == '>' and top != '<') :
                return ''
    
    completion = ""
    while stack:
        top = stack.pop()
        if top == '(':
            completion += ')' 
        elif top == '[':
            completion += ']'
        elif top == '{':
            completion += '}'
        elif top == '<':
            completion += '>'
    
    return completion
    

def ac_score(cstr):
    '''AutoComplete Score takes a completion string and scores it according to rules'''
    score = 0
    for char in cstr:
        score *= 5
        score += SCORE_TABLE_COMPLETION[char]
    return score