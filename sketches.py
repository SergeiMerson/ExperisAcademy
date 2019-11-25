# Get file from disk:
book_path = r"d:\Projects\ExperisAcademy\Exercises\Project_Gutenberg\The_Black_Arrow.txt"
stopwords_path = r"d:\Projects\ExperisAcademy\Exercises\Project_Gutenberg\stopwords.txt"


def get_stopwords(stopwords_path):
    with open(stopwords_path, 'r', encoding='UTF-8') as stopwords_file:
        return set([symbol.strip() for symbol in stopwords_file.readlines()])


def get_non_chars():
    non_chars = {chr(i) for i in range(32,65)}
    # non_chars.discard('-')
    return ''.join(non_chars)


def process_line(line:str, non_chars:str, stopwords:set, vocabulary:dict):
    # Initialize dict to store result:

    # Split, convert to lowercase and strip:
    words = [word.strip(non_chars).lower() for word in line.split()]

    # Iterate over each word:
    for word in words:
        # Append only words that not in stopwords:
        if word not in stopwords:
            vocabulary[word] = vocabulary.get(word, 0) + 1

    return vocabulary


def count_words(book_path, stopwords_path):

    stopwords = get_stopwords(stopwords_path)
    non_chars = get_non_chars()
    vocabulary = {}

    with open(book_path, 'r', encoding='UTF-8') as book_file:
        current_line = book_file.readline()

        while current_line:
            vocabulary = process_line(current_line, non_chars, stopwords, vocabulary)
            current_line = book_file.readline()

    # Reverse vocabulary:
    result = {val: key for key, val in vocabulary.items()}

    return result


for num, word in count_words(book_path, stopwords_path).items():
    print(num, word, sep='\t')