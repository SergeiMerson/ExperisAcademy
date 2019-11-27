import uuid
import random
import pickle


class Author:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.author_id = ''.join(random.choices(first_name + second_name, k=4)) + str(random.choice(range(1000, 9999)))


class Book:
    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id
        self.book_id = str(uuid.uuid1())


class Register:
    def __init__(self):
        self.register = {}

    def get_items(self):
        return ((val, key) for key, val in self.register.items())

    def reset_register(self):
        user_input = input('Do you really want to reset the Register and delete all records? [Y]/[N]: ')
        if user_input.lower() == 'y':
            self.register.clear()
            print('The Register was reset successfully')


class AuthorRegister(Register):

    def add_author(self, first_name, second_name):
        author = Author(first_name, second_name)
        self.register[author.author_id] = author
        print(f'Successfully added {first_name} {second_name} to the Register with ID: {author.author_id}')

    def remove_author(self, author_id):
        try:
            author = self.register[author_id]
            del self.register[author_id]
            print(f'Successfully removed {author.first_name} {author.second_name} with ID: {author_id} form Register')
        except KeyError:
            print(f'There is no Author with ID: {author_id}')


class BookRegister(Register):

    def add_book(self, title, author_id):
        book = Book(title, author_id)
        self.register[book.book_id] = book

    def remove_book(self, book_id):
        try:
            book_title = self.register[book_id].title
            del self.register[book_id]
            print(f'Successfully deleted Book {book_title} with id: {book_id}')
        except KeyError:
            print(f'There is no Book with ID: {book_id}')

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

    def save_library(self):
        with open('library_manager.pkl', 'w') as file:
            pickle.dump((self.authors, self.books), file)

    def load_library(self):
        with open('library_manager.pkl', 'r') as file:
            self.authors, self.books = pickle.load(file)


class TUI:
    @classmethod
    def border_decorator(cls, func):



    def print_register