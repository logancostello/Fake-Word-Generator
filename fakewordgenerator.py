def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = list(word_file.read().split())
    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print(english_words)