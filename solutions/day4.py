from functools import reduce
from utils.reading import file_to_list_of_lines
def solve():
    # puz_input = file_to_list_of_lines('inputs/test4.txt')
    puz_input = file_to_list_of_lines('inputs/4.txt')
    draw_line = puz_input.pop(0)
    draw_list = draw_line.split(',')

    boards = input_to_boards(puz_input)
    # print(boards[0])
    marked = [[[False, False, False, False, False] for _ in range(5)] for _ in range(len(boards))]

    game_over = False
    boards_have_won = [False for _ in range(len(boards))]
    while not game_over:
        num = draw_list.pop(0)
        mark_num(boards, marked, num)
        for i,board in enumerate(marked):
            bwon = board_has_win(board)
            if bwon:
                boards_have_won[i] = True
            havent_won = boards_have_won.count(False)
            if havent_won == 1:
                game_over = True
                last_board_id = boards_have_won.index(False)
    
    while not board_has_win(marked[last_board_id]):
        num = draw_list.pop(0)
        mark_num(boards, marked, num)
    
    score = score_board(boards[last_board_id], marked[last_board_id])
    print(num)
    print(int(num) * score)
    print(last_board_id)

    board_score = score_board(boards[i], marked[i])

def score_board(board, mark):
    score = 0
    for r in range(5):
        for c in range(5):
            if not mark[r][c]:
                score += int(board[r][c])
    return score

def mark_num(boards, marks, num):
    for b in range(len(boards)):
        for r in range(len(boards[0])):
            for c in range(len(boards[0][0])):
                if boards[b][r][c] == num:
                    marks[b][r][c] = True

def board_has_win(board_marks):
    # check if any rows are fully marked
    for row in board_marks:
        row_wins = reduce(both_true, row)
        if row_wins: 
            return True
    # check if any columns are fully marked
    for col in range(5):
        col_wins = reduce(both_true, [board_marks[i][col] for i in range(5)])
        if col_wins:
            return True
    return False


def input_to_boards(input):
    lines_separated = []
    for i in range(1, len(input), 6):
        lines_separated.append(input[i:i+5])

    boards = []
    for line in lines_separated:
        board_next = []
        for row in line:
            row_next = row.split()
            board_next.append(row_next)
        boards.append(board_next)
    return boards

def both_true(a,b):
    return bool(a and b)

if __name__ == '__main__':
    solve()