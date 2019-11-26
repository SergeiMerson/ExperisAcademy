def get_stopwords(stopwords_path):
    with open(stopwords_path, 'r', encoding='UTF-8') as stopwords_file:
        return set([symbol.strip() for symbol in stopwords_file.readlines()])


def get_non_chars():
    ascii_non_chars = list(range(0,65)) + list(range(91,97)) + list(range(123,128))
    ascii_val_chars = list(range(65,91)) + list(range(97,123))
    non_chars = (chr(i) for i in ascii_non_chars)
    val_chars = {chr(i) for i in ascii_val_chars}
    return ''.join(non_chars), val_chars


def clear_non_chars(word, non_chars, val_chars):
    if not word.isalpha():
        word = word.strip(non_chars)
        word = word[:-2] if word[-2:] in ('’s','’d') else word
        word = word[:-3] if word[-3:] in ('’st','’d') else word
        word = ''.join([letter for letter in word if letter in val_chars])
        return word


def acceptable_word(word, stopwords):
    return (word is not None) and (word not in stopwords) and (len(word) > 0)


def split_line(line, delimiters):
    for d in delimiters:
        line = line.replace(' '+d, ' ')
    list_of_words = line.split()
    return list_of_words
