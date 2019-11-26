from Exercises.Project_Gutenberg import cleantext


def process_line(line: str, non_chars: str, val_chars, stopwords: str, vocabulary: dict):
    # Split and convert to lowercase:
    list_of_words = cleantext.split_line(line, ['—'])

    # Iterate over each word:
    for word in list_of_words:
        word = word.lower()
        word = cleantext.clear_non_chars(word, non_chars, val_chars)
        # Append only words that not in stopwords:
        if cleantext.acceptable_word(word, stopwords):
            vocabulary[word] = vocabulary.get(word, 0) + 1

    return vocabulary


def count_words(book_path, stopwords_path):
    stopwords = cleantext.get_stopwords(stopwords_path)
    non_chars, val_chars = cleantext.get_non_chars()
    vocabulary = {}

    with open(book_path, 'r', encoding='UTF-8') as book_file:
        current_line = book_file.readline()

        while current_line:
            vocabulary = process_line(current_line, non_chars, val_chars, stopwords, vocabulary)
            current_line = book_file.readline()

    # Print result in descending order:
    for key, val in sorted(vocabulary.items(),
                           key=lambda key_val: (key_val[1], (key_val[0])),
                           reverse=True):
        print(f'{key:<15s} {val:<4d}', sep='\t')

    return vocabulary


if __name__ == '__main__':
    # Get file from disk:
    book_path = r"d:\Projects\ExperisAcademy\Exercises\Project_Gutenberg\Macbeth.txt"
    stopwords_path = r"d:\Projects\ExperisAcademy\Exercises\Project_Gutenberg\stopwords.txt"
    count_words(book_path, stopwords_path)
