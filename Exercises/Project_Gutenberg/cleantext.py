def get_stopwords(stopwords_path):
    with open(stopwords_path, 'r', encoding='UTF-8') as stopwords_file:
        return set([symbol.strip() for symbol in stopwords_file.readlines()])


def get_non_chars():
    non_chars = {chr(i) for i in range(32,65)}
    non_chars.update({chr(i) for i in range(91, 97)})
    non_chars.update({chr(i) for i in range(123, 128)})
    # non_chars.discard('-')
    return ''.join(non_chars)


def clear_non_chars(word, non_chars):
    if not word.isalpha():
        word = ''.join([letter for letter in word if letter not in non_chars])
        return word


def process_line(line:str, non_chars:str, stopwords:set, vocabulary:dict):
    # Split, convert to lowercase and strip:
    words = [word.strip(non_chars).lower() for word in line.split()]

    # Iterate over each word:
    for word in words:
        #word = clear_non_chars(word, non_chars)
        # Append only words that not in stopwords:
        if (word not in stopwords) and (word is not None):
            vocabulary[word] = vocabulary.get(word, 0) + 1

    return vocabulary
