def cell_is_suitable(row, col, queens_on_board):
    horizontal_check = any((row == queen[0] for queen in queens_on_board))
    vertical_check = any((col == queen[1] for queen in queens_on_board))
    diagonal_check = any((abs(row - queen[0]) == abs(col - queen[1]) for queen in queens_on_board))
    return not any((horizontal_check, vertical_check, diagonal_check))


def count_queens(row, board_size, queens_on_board=[], answer=0):

    found_allocation = False
    col = 0
    while (not found_allocation) and (col < board_size):
        found_allocation = cell_is_suitable(row, col, queens_on_board)
        if found_allocation:
            queens_on_board.append((row, col))
        col += 1

    if row + 1 == len(queens_on_board) == board_size:
        return 1
    elif row == board_size - 1:
        return 0
    else:
        answer += count_queens(row + 1, board_size, queens_on_board)
    return answer


def eight_queens():
    ans = count_queens(0, 4, [])
    return ans


def new_screen(func):
    def orig_func(*args):
        print('+' + '-' * 82 + '+')
        print('|' + '-' * 82 + '|')
        func(*args)
        print('+' + '-' * 82 + '+')
        print('|' + '-' * 82 + '|')
    return orig_func()



def celcius_to_farenheit(func):
    return lambda *args: 1.8 * func(*args) + 32

@celcius_to_farenheit
@new_screen
def get_temp(a, b):
    print( a * b)

# ---------------------------------------------


def celcius_to_farenheit(func):
    def far_func(*args):
        return 1.8 * func(*args) + 32
    return far_func

@celcius_to_farenheit
def get_temp():
    return 36.6


class Decorators:
    @classmethod
    def decorate_print(cls, title='', dims=(82, 30)):
        def wrapper(func):
            def inner_func(*args, **kwargs):
                print('\n' * dims[1], f"{(' ' + str(title) + ' ').center(dims[0], '=')}", '\n', sep='')
                func(*args, **kwargs)
                return func

            return inner_func

        return wrapper