from utils.reading import file_to_list_of_lines
from collections import deque

SCORE_TABLE = {
    ')' :3,
    ']': 57 ,
    '}': 1197 ,
    '>': 25137 
}

def solve():
    input = file_to_list_of_lines("inputs/10.txt")
    score = 0
    for line in input:
        bad = process_line(line)
        if bad:
            score += SCORE_TABLE[bad]
    print(f"Score: {score}")

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
                return ch
    # if stack:
    #     print("incomplete")
    # else:
    #     print("seems ok")