def _print_header(title='', width=120):
    print('\n' * 30, f"{(' ' + str(title) + ' ').center(width, '=')}", '\n', sep='')


def _print_closure(width=120):
    print('\n', '=' * width, sep='')


def print_menu(title, options, width=120):
    _print_header(title=title, width=width)
    for i, opt in enumerate(options, 1):
        print(f"{str(i):>4s} : {opt}")
    _print_closure(width)
    user_answer = False
    while not user_answer:
        try:
            user_answer = int(input('Please enter your choice: '))
        except ValueError:
            print('Cannot understand your input, please try again:')
    return user_answer


def print_list_of_items(title, lst, width=120):
    _print_header(title=title, width=width)
    max_len_0 = max(map(len, [row[0] for row in lst]))
    max_len_1 = max(map(len, [row[1] for row in lst]))
    for row in lst:
        print(' '*4 + f"{str(row[0]):<{max_len_0}}",
              f"{str(row[1]):<{max_len_1}}",
              *row[2:], sep=' '*4)
    _print_closure(width=width)

