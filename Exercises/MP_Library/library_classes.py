import pickle
import json
import base_classes as bc
import TUI as tui


class Library:
    def __init__(self):
        self.authors = bc.AuthorRegister()
        self.books = bc.BookRegister()

    # -------------------------- Search --------------------------- #

    def search_books_by_author(self, first_name='?', last_name='?'):
        author = self.search_author(first_name, last_name)
        if author:
            list_of_results = []
            book_list = self.books.search_by_author(author.id)
            for book in book_list:
                list_of_results.append([book.id, book.title, author.first_name + ' ' + author.last_name])
            if book_list:
                tui.print_list_of_items(f"Search results for: {first_name} {last_name}", list_of_results)
                return author, book_list
            else:
                print(f"There is no books of {first_name} {last_name} in the Registry")

    def search_book_by_title(self, title):
        list_of_results = []
        book_list = self.books.search_by_title(title)
        for book in book_list:
            author = self.authors.register[book.author_id]
            list_of_results.append([book.id, book.title, author.first_name + ' ' + author.last_name])
        if book_list:
            tui.print_list_of_items(f"Search results for: {title}", list_of_results)
        else:
            print(f"Nothing was found for '{title}'")

    def search_author(self, first_name, last_name):
        # Get the list of existing authors:
        author_list = self.authors.search_by_name(first_name, last_name)
        if author_list:
            print('There are several authors with such name:')
            for ind, a in enumerate(author_list, 1):
                print(f'{ind}:', a.first_name, a.last_name)
            user_answer = input('Do you want to choose existing record [index]/[N]? ')
            try:
                user_answer = int(user_answer)
                author = author_list[user_answer - 1]
            except KeyError:
                print(f"There is no author with such index: {user_answer}")
                author = None
            except ValueError:
                print(f"Adding a new record for {first_name} {last_name}")
                author = None
        else:
            author = None
            print(f'There is no author {first_name} {last_name} in the Register')
        return author

    # ------------------------ Add / Delete ----------------------- #

    def add_author(self, first_name, last_name):
        # Get the list of existing authors:
        author = self.search_author(first_name, last_name)
        if not author:
            author = self.authors.add(first_name, last_name)
        else:
            print(f"Selected {author.first_name} {author.last_name}, ID: {author.id}")
        return author

    def remove_author(self, first_name, last_name):
        try:
            author, book_list = self.search_books_by_author(first_name, last_name)
            user_input = input(f'Do you really want to delete all records '
                               f'for {first_name} {last_name}? [Y]/[N]: ')
            if user_input.lower() == 'y':
                for book in book_list:
                    del self.books.register[book.id]
                del self.authors.register[author.id]
        except TypeError:
            pass

    def add_book(self, title, first_name, last_name):
        # Select or add new author:
        author = self.add_author(first_name, last_name)
        _ = self.books.add_book(title, author.id)

    # ---------------------------- I/O ---------------------------- #

    def save_library(self):
        with open('library_manager.pkl', 'wb') as file:
            pickle.dump((self.authors, self.books), file)
            print('Library was successfully saved on disk')

    def load_library(self):
        with open('library_manager.pkl', 'rb') as file:
            self.authors, self.books = pickle.load(file)

    def export_library(self):
        library_records = {}
        for _, book in self.books.register.items():
            author = self.authors.register[book.author_id]

            if not library_records.get(author.id, False):
                library_records[author.id] = {'first_name': author.first_name,
                                              'last_name': author.last_name,
                                              'books': []}

            library_records[author.id]['books'].append((book.id, book.title))
        with open('library_export.json', 'w') as json_file:
            json.dump(library_records, json_file)
            print('All the records were exported successfully!')
