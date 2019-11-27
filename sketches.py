def count_queens(row, board_size, queens_on_board, answer):

    found_allocation = False
    col = 0
    while (not found_allocation) or (col < board_size):
        found_allocation = cell_is_suitable(row, col)
        if found_allocation:
            queens_on_board.append((row, col))
        col += 1

    if row == len(queens_on_board) == board_size - 1:
        return 1
    elif row == board_size - 1:
        return  0
    else:
        answer += count_queens(row + 1, board_size, queens_on_board)
    return answer



def setup_board(N):
    current_allocations = []
    return


def cell_is_suitable(row, col, queens_on_board):
    horizontal_check = any((row == queen[0] for queen in queens_on_board))
    vertical_check = any((col == queen[1] for queen in queens_on_board))
    diagonal_check = any((abs(row - queen[0]) == abs(col - queen[1]) for queen in queens_on_board))
    return not any((horizontal_check, vertical_check, diagonal_check))