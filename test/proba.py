import unittest

from Dictionary.Pos import Pos

from WordNet.WordNet import WordNet


class UzbekWordNetTest(unittest.TestCase):
    uzbek: WordNet

    def setUp(self) -> None:
        self.uzbek = WordNet("../turkish_wordnet.xml")
        # self.uzbek = WordNet()

    # def test_SynSetList(self):
    #     literalCount = 0
    #     for synSet in self.uzbek.synSetList():
    #         literalCount += synSet.getSynonym().literalSize()
    #     self.assertEquals(109049, literalCount)

    # def test_LiteralList(self):
        # self.assertEquals(81092, len(self.uzbek.literalList()))

    def test_GetSynSetWithId(self):
       print(self.uzbek.getSynSetWithId("UZBEK10-0000010"))


    def test_GetSynSetWithLiteral(self):
        # self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("sıradaki", 1))
        print(self.uzbek.getSynSetWithLiteral("suv", 1))
        print(1, self.uzbek.numberOfSynSetsWithLiteral("suv"))



if __name__ == '__main__':
    unittest.main()
