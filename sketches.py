def check_horizontal(row, queens_on_board):
    return any(row == queen[0] for queen in queens_on_board)


def check_vertical(col, queens_on_board):
    return any(col == queen[1] for queen in queens_on_board)


def check_diagonal(row, col, queens_on_board):
    return any([abs(row - queen[0]) == abs(col - queen[1]) for queen in queens_on_board])


def cell_is_suitable(row, col, queens_on_board):
    return not any([
        check_horizontal(row, queens_on_board),
        check_vertical(col, queens_on_board),
        check_diagonal(row, col, queens_on_board)
    ])


def count_allocations(board_size, queens_on_board, current_row = 0, allocations_found = 0):
    for row in range(current_row, board_size):
        position_found = False
        while not position_found:
            for col in range(board_size):
                position_found = cell_is_suitable(row, col,queens_on_board)
                if position_found:
                    queens_on_board.append((row, col))

                if len(queens_on_board) == board_size:
                    allocations_found += 1
                elif len(queens_on_board) < board_size:
                    allocations_found += count_allocations(
                        board_size,
                        queens_on_board,
                        current_row+1,allocations_found)
    return allocations_found


count_allocations(4, [])





















def find_new_position(board_size, queens_on_board, current_row=0):
    for row in range(current_row, board_size):
        position_found = False
        while not position_found:
            for col in range(board_size):
                position_found = cell_is_suitable(row, col,queens_on_board)
                if position_found:
                    result



            pass


def calc_num_of_allocations(N_queens):
    result = 0
    res


