from random import *

ROWS = 4
COLUMNS = 8

def run_chomp():
    board = create_board(ROWS, COLUMNS)
    print_board(board)

def create_board(rows: int, columns: int) -> list[list[int]]:
    board = [[1] * columns for _ in range(rows)]

    poisened_row = randint(0, rows - 1)
    poisened_column = randint(0, columns -1)

    board[poisened_row][poisened_column] = 0

    return board

def print_board(board) -> None:
    for row in board:
        for item in row:
            print(item, end=" ")
        print("")


if __name__ == "__main__":
    run_chomp()