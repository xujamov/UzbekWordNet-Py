# function to find all adjectives from turkish wordnet
def test_sort_words(self):
    f = open("../turkish_wordnet.xml")
    key = "<POS>a</POS>"
    for line in f:
        if key in line:
            with open("wordnet_adj_turkish.txt", 'a', encoding='utf-8') as w:
                w.write(line)


if __name__ == '__main__':
    test_sort_words()
