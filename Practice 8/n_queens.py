def place_queens(n):
    board = [[False] * n for _ in range(n)]

    sol = place_queens_helper(board, 0)
    # if sol:
        # print(board)
    return board

def place_queens_helper(board, column):
    if column == len(board[0]):
        return True

    for row in range(len(board)):
        if not is_valid(board, row, column):
            continue

        board[row][column] = True
        if place_queens_helper(board, column + 1):
            return True
        board[row][column] = False
    return False

def is_valid(board, row, column):
    for i in range(len(board)):
        if board[i][column] and i != row:
            return False

    for j in range(len(board[row])):
        if board[row][j] and j != column:
            return False
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] and abs(i - row) == abs(j - column):
                return False

    return True


print(place_queens(8))