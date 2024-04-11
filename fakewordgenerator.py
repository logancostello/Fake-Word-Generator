def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = list(word_file.read().split())
    return valid_words


def create_empty_edge_list():
    # create hashmap with english letters as keys (nodes in our graph)
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    graph = {letter: 0 for letter in letters + ['.']}

    # set values to hashmap for tracking frequencies of following chars
    freq = graph.copy()
    for key in graph:
        graph[key] = freq.copy()

    return graph


def count_frequencies(words, graph):
    # read through all words and update frequencies
    for word in words:
        for i in range(len(word) - 1):
            graph[word[i]][word[i + 1]] += 1
        graph[word[-1]]['.'] += 1


if __name__ == '__main__':
    english_words = load_words()
    word_graph = create_empty_edge_list()
    count_frequencies(english_words, word_graph)
    print(word_graph['a']['.'])
