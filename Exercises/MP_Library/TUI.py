class TUI_print:

    @staticmethod
    def _print_header(self, title='', width=82):
        print('\n' * 30, f"{(' ' + str(title) + ' ').center(width, '=')}", '\n', sep='')

    @staticmethod
    def _print_closure(self, width=82):
        print('\n', '=' * width, sep='')

    def print_menu(self, title, options, width=82):
        TUI_print._print_header(self, title=title, width=width)
        for i, opt in enumerate(options, 1):
            print(f"{str(i):>4s} : {opt}")
        TUI_print._print_closure(width)
        user_answer = False
        while not user_answer:
            try:
                user_answer = int(input('Please enter your choice: '))
            except ValueError:
                print('Cannot understand your input, please try again:')
        return user_answer

    def print_list_of_items(self, title, lst, width=82):
        TUI_print._print_header(self, title=title, width=width)
        max_len_0 = max(map(len, [row[0] for row in lst]))
        max_len_1 = max(map(len, [row[1] for row in lst]))
        for row in lst:
            print(' '*4 + f"{str(row[0]):<{max_len_0}}\t{str(row[1]):<{max_len_1}}", *row[2:], sep='\t')
        TUI_print._print_closure(self, width=width)

