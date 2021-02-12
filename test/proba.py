import unittest

from Dictionary.Pos import Pos

from WordNet.WordNet import WordNet


class UzbekWordNetTest(unittest.TestCase):
    uzbek: WordNet

    def setUp(self) -> None:
        self.uzbek = WordNet("../uzbek_adjective.xml")
        # self.uzbek = WordNet()

    def test_wordsList(self):
        cnt = 0
        # for elem in self.uzbek.literalList():
        #     cnt += 1
        #     print(cnt, elem)
        with open('../uzbek_adjective.xml', 'r') as f:
            for line in f.readlines():
                ind = line.find('<SENSE>')
                with open('adj_words.txt', 'a') as w:
                    w.write(line[48:ind] + '\n')

    # def test_SynSetList(self):
    #     literalCount = 0
    #     for synSet in self.uzbek.synSetList():
    #         literalCount += synSet.getSynonym().literalSize()
    #     self.assertEquals(109049, literalCount)

    # def test_LiteralList(self):
        # self.assertEquals(81092, len(self.uzbek.literalList()))

    # def test_GetSynSetWithId(self):
    #    print(self.uzbek.getSynSetWithId("UZBEK10-0000010"))


    def test_GetSynSetWithLiteral(self):
        # self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("sıradaki", 1))
        print(self.uzbek.getSynSetWithLiteral("abad", 1))
        print(1, self.uzbek.numberOfSynSetsWithLiteral("abad"))



if __name__ == '__main__':
    unittest.main()
