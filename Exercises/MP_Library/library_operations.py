def add_author(first_name, second_name, author_register):
    # Check that there is no such author exists:
    if (first_name, second_name) in author_register.get_list_of_authors():
        print('There already exits Author with such name')