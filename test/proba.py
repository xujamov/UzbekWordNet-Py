import unittest

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
    # def test_wordsToXML(self):
    #     cnt = 0
    #     # for elem in self.uzbek.literalList():
    #     #     cnt += 1
    #     #     print(cnt, elem)
    #     words = []
    #     with open('adj_words_uzb.txt', 'r') as f:
    #         for line in f.readlines():
    #             words.append(line)
    #     definitions = []
    #     with open('adj_definition_uzb.txt', 'r') as f:
    #         for line in f.readlines():
    #             definitions.append(line)
    #     with open('../uzbek_adjective.xml', 'r') as f:
    #         for line in f.readlines():
    #             ind = line.find('<SENSE>')
    #             ind2 = line.find('<DEF>') + 5
    #             ind3 = line.find('</DEF>')
    #             with open('wordnet_adj_uzb.xml', 'a') as w:
    #                 if cnt < 300:
    #                     w.write(line[0:48] + words[cnt].rstrip('\n') + line[ind:ind2] +
    #                             definitions[cnt].rstrip('\n') + line[ind3::])
    #                 cnt += 1


    # def test_SynSetList(self):
    #     literalCount = 0
    #     for synSet in self.uzbek.synSetList():
    #         literalCount += synSet.getSynonym().literalSize()
    #     self.assertEquals(109049, literalCount)

    def test_SynSetSynonymList(self):
        for synSet in self.uzbek.synSetList():
            synSet.getSynonym().literalSize()
            for i in range(synSet.getSynonym().literalSize()):
                literal = synSet.getSynonym().getLiteral(i)
                print(f'{i}: {literal}')

    # def test_LiteralList(self):
        # self.assertEquals(81092, len(self.uzbek.literalList()))

    # def test_GetSynSetWithId(self):
    #    print(self.uzbek.getSynSetWithId("UZBEK10-0000010"))


    # def test_GetSynSetWithLiteral(self):
    #     # self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("sıradaki", 1))
    #     word = "shafqatsiz"
    #     word2 = "qobiliyatsiz"
    #     print(word + ": ", self.uzbek.getSynSetWithLiteral(word, 2))
    #     print(word2 + ": ", self.uzbek.getSynSetWithLiteral(word2, 3))
    #     # print(word.getSynonym().literalSize())
    #     literalCount = 0
    #     cnt = 0
    #     for synSet in self.uzbek.synSetList():
    #         cnt += 1
    #         print(str(synSet.getSynonym())
    #               + ", literalSize: " + synSet.getSynonym().literalSize())
    #         print(cnt, synSet)
    #         literalCount += synSet.getSynonym().literalSize()
        # print(literalCount)
        # print(self.uzbek.numberOfSynSetsWithLiteral(word))



if __name__ == '__main__':
    unittest.main()
