

call_func = {100: menu_main,

             200: menu_books, 201: add_book, 202: remove_book, 203: search_book_by_id,
             204: search_book_by_title, 205: search_book_by_author,

             300: menu_authors, 301: add_author, 302: remove_author, 303: search_author_by_id,
             304: search_author_by_name, 305: search_book_by_author,

             400: menu_search, 401:search_author_by_id, 402:search_author_by_name,
             403:search_book_by_id, 404:search_book_by_title, 405:search_book_by_author,

             500: menu_IO, 501:export_to_json, 502:save, 503:load}

call_codes = {
                 100: {1: 200, 2:300, 3:400, 4:500, 9:999},
                 200: {0: 100, 1:201, 2:202, 3:203, 4:204, 5:205, 9:999},
                 300: {0: 100, 1:301, 2:302, 3:303, 4:304, 5:305, 9:999},
                 400: {0: 100, 1:401, 2:402, 3:403, 4:404, 5:405, 9:999},
                 500: {0: 100, 1:501, 2:502, 3:503, 9:999}}

current_screen = 100
while current_screen != 999:
    call_codes[current_screen]()