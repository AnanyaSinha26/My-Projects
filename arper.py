def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
            board[row] = -1

    return False

def print_board(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

a = int(input("Please enter an integer number: "))
board = [-1] * a
solve(board, 0)
print_board(board)
