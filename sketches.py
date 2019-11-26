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


def find_new_position(queens_on_board, current_row = 8):
    for row in range(current_row):
        for col in range(1):
            pass


def calc_num_of_allocations(N_queens):
    result = 0














def go_to_location(player, direction):
    try:
        player['location'] = player['location']['connections'][direction]
    except KeyError:
        print(f'There is nothing on {direction}')



def exep_tions():
    a = 0
    lst = [6,7,8]
    try:
        print(5/a)
    except ZeroDivisionError:
        print('Divide by zero...')
        return
    else:
        print('else')
    finally:
        print('finaly!')




