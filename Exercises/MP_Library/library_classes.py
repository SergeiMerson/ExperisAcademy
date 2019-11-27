import random
import pickle


def generate_id():
    letters = [chr(l) for l in list(range(65, 91)) + list(range(97, 123))]
    return ''.join(random.choices(letters, k=5)) + str(random.choice(range(int(1e5), int(1e6))))


class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = generate_id()


class Book:
    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id
        self.id = author_id + '-' + generate_id()


class Register:
    def __init__(self):
        self.register = {}

    def get_items(self):
        return (val for _, val in self.register.items())

    def get_by_key(self, key):
        try:
            return self.register[key]
        except KeyError:
            print('There is no such key')

    def reset_register(self):
        user_input = input('Do you really want to reset the Register and delete all records? [Y]/[N]: ')
        if user_input.lower() == 'y':
            self.register.clear()
            print('The Register was reset successfully')


class AuthorRegister(Register):

    def add(self, first_name, last_name):
        author = Author(first_name, last_name)
        self.register[author.id] = author
        print(f'Successfully added {first_name} {last_name} to the Register with ID: {author.id}')
        return author

    def remove_author(self, author_id):
        try:
            author = self.register[author_id]
            del self.register[author_id]
            print(f'Successfully removed {author.first_name} {author.last_name} with ID: {author_id} form Register')
        except KeyError:
            print(f'There is no Author with ID: {author_id}')

    def search_by_name(self, first_name='?', last_name='?'):
        operator = any if any((first_name == '?', last_name == '?')) else all
        return [a for a in self.get_items()
                if operator((
                    first_name.lower() in a.first_name.lower(),
                    last_name.lower() in a.last_name.lower()
                ))]


class BookRegister(Register):

    def add_book(self, title, author_id):
        book = Book(title, author_id)
        self.register[book.id] = book
        return book

    def remove_book(self, book_id):
        try:
            book_title = self.register[book_id].title
            del self.register[book_id]
            print(f'Successfully deleted Book {book_title} with id: {book_id}')
        except KeyError:
            print(f'There is no Book with ID: {book_id}')

    def search_by_title(self, title):
        return [b for b in self.get_items() if title.lower() in b.title.lower()]

    def get_book_info(self, book_id):
        try:
            book = self.register[book_id]
            print(f'+--------------------------------------------------+')
            print(f'| Title:    {book.title:<38s} |')
            print(f'| AuthorID: {book.author_id:<38s} |')
            print(f'+--------------------------------------------------+')
        except KeyError:
            print(f'There is no book with such ID: {book_id}')


# =================================================================================


class Library:
    def __init__(self):
        self.authors = AuthorRegister()
        self.books = BookRegister()

    def add_book(self, title, first_name, last_name):
        # Select or add new author:
        author = self.add_author(first_name, last_name)
        _ = self.books.add_book(title, author.id)

    def add_author(self, first_name, last_name):
        # Get the list of existing authors:
        author_list = self.authors.search_by_name(first_name, last_name)
        if not author_list:
            author = self.authors.add(first_name, last_name)
        else:
            print('There are several authors with such name:')
            for ind, a in enumerate(author_list, 1):
                print(f'{ind}:', a.first_name, a.last_name)
            user_answer = input('Do you want to choose existing record [index] or create a new one [other]? ')
            try:
                author = author_list[int(user_answer) - 1]
            except KeyError or ValueError:
                author = self.authors.add(first_name, last_name)
        return author

    def save_library(self):
        with open('library_manager.pkl', 'wb') as file:
            pickle.dump((self.authors, self.books), file)
            print('Library was successfully saved on disk')

    def load_library(self):
        with open('library_manager.pkl', 'rb') as file:
            self.authors, self.books = pickle.load(file)

    def search_by_title(self, title):
        result = self.books.search_by_title(title)
        for book in result:
            author = self.authors.register[book.author_id]
            print(f'Title: {book.title}, author: {author.first_name} {author.last_name}')


class TUI:
    class Decorators:
        @classmethod
        def new_screen(func):
            def orig_func(*args):
                return func(*args)

            print()

    def __init__(self, authors, books):
        self.authors = authors
        self.books = books
        self.width = 82
        self.height = 62

    def print_items(self, authors):
        print('+' + '-' * 82 + '+')
        print
        for key, value in authors.items():
            print
