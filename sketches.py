from Exercises.Project_Gutenberg import cleantext


# Get file from disk:
book_path = r"d:\Projects\ExperisAcademy\Exercises\Project_Gutenberg\Macbeth.txt"
stopwords_path = r"d:\Projects\ExperisAcademy\Exercises\Project_Gutenberg\stopwords.txt"


def count_words(book_path, stopwords_path):

    stopwords = cleantext.get_stopwords(stopwords_path)
    non_chars = cleantext.get_non_chars()
    vocabulary = {}

    with open(book_path, 'r', encoding='UTF-8') as book_file:
        current_line = book_file.readline()

        while current_line:
            vocabulary = cleantext.process_line(current_line, non_chars, stopwords, vocabulary)
            current_line = book_file.readline()

    # # Reverse vocabulary:
    # result = {val: key for key, val in vocabulary.items()}

    # Print result in descending order:
    for key, val in sorted(vocabulary.items(),
                      key=lambda key_val: (key_val[1], (key_val[0])),
                      reverse=True):
        print(f'{key:<15s} {val:<4d}', sep='\t')

    return vocabulary


if __name__ == '__main__':
    count_words(book_path, stopwords_path)