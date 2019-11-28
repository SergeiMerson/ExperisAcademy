
call_codes = {100: 'main_menu',
              200: 'books',
              300: 'authors',
              400: 'search',
              500: 'I/O',
              999: 'exit'}

current_screen = 100
while current_screen != 999:
    call_codes[current_screen]()