import uuid
import random
import json


class Book():
    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id
        self.book_id = str(uuid.uuid1())


class BookRegister:
    def __init__(self):
        self.book_register = {}

    def add_book(self, title, author_id):
        book = Book(title, author_id)
        self.book_register[book.book_id] = book

    def remove_book(self, book_id):
        try:
            book_title = self.book_register[book_id].title
            del self.book_register[book_id]
            print(f'Successfully deleted Book {book_title} with id: {book_id}')
        except KeyError:
            print(f'There is no Book with ID: {book_id}')

    def get_book_info(self, book_id):
        try:
            book = self.book_register[book_id]
            print(f'+--------------------------------------------------+')
            print(f'| Title:    {book.title:<38s} |')
            print(f'| AuthorID: {book.author_id:<38s} |')
            print(f'+--------------------------------------------------+')
        except:
            print(f'There is no book with such ID: {book_id}')

# =================================================================================


class Author:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.author_id = ''.join(random.choices(first_name + second_name, k=4)) + str(random.choice(range(1000, 9999)))


class AuthorRegister:
    def __init__(self):
        self.author_index = {}

    def add_author(self, first_name, second_name):
        author = Author(first_name, second_name)
        self.author_index[author.author_id] = author
        print(f'Successfully added {first_name} {second_name} to the Register with ID: {author.author_id}')

    def remove_author(self, author_id):
        try:
            author = self.author_index[author_id]
            del self.author_index[author_id]
            print(f'Successfully removed {author.first_name} {author.second_name} with ID: {author_id} form Register')
        except KeyError:
            print(f'There is no Author with ID: {author_id}')

    def reset_register(self):
        user_input = input('Do you really want to reset the Register and delete all records? [Y]/[N]: ')
        if user_input.lower() == 'y':
            self.author_index.clear()
            print('The author register was reset successfully')

    def get_list_of_authors(self):
        return ((val, key) for key, val in self.author_index.items())
