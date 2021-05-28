import unittest
import csv

from Dictionary.Pos import Pos

from WordNet.WordNet import WordNet


class UzbekWordNetTest(unittest.TestCase):
    uzbek: WordNet

    def setUp(self) -> None:
        self.uzbek = WordNet("wordnet_adj_uzb.xml")
        # self.uzbek = WordNet()

    # def test_wordsList(self):
    #     cnt = 0
    #     # for elem in self.uzbek.literalList():
    #     #     cnt += 1
    #     #     print(cnt, elem)
    #     with open('../uzbek_adjective.xml', 'r') as f:
    #         for line in f.readlines():
    #             ind = line.find('<SENSE>')
    #             with open('adj_words_turkish.txt', 'a') as w:
    #                 w.write(line[48:ind] + '\n')
    #
    def test_searchingWordsFromDb(self):
        cnt = 0
        # for elem in self.uzbek.literalList():
        #     cnt += 1
        #     print(cnt, elem)
        words = []
        with open('adj_words_uzb.txt', 'r') as f:
            for line in f.readlines():
                words.append(line.rstrip())

        with open('words_db.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            words_found = 0
            head = True
            for row in csv_reader:
                if head:
                    print(f'Column names are {", ".join(row)}')
                    head = False
                if row[1] in words:
                    words_found += 1
                    print(f'{words_found}: {row[1]} ma\'nosi {row[4]}')
            print(f'Found {words_found} words.')

if __name__ == '__main__':
    unittest.main()
