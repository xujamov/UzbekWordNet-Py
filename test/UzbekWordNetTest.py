import unittest

from Dictionary.Pos import Pos

from WordNet.WordNet import WordNet


class WordNetTest(unittest.TestCase):
    uzbek: WordNet

    def setUp(self) -> None:
        self.uzbek = WordNet("../uzbek_wordnet.xml")

    def test_SynSetList(self):
        literalCount = 0
        for synSet in self.uzbek.synSetList():
            literalCount += synSet.getSynonym().literalSize()
        self.assertEquals(109049, literalCount)

    # def test_LiteralList(self):
    #     self.assertEquals(81092, len(self.uzbek.literalList()))
    #     cnt = 0
    #     for elem in self.uzbek.literalList():
    #         print(cnt, elem, self.uzbek.getSynSetWithLiteral(elem, 1))
    #         cnt += 1

    def test_GetSynSetWithId(self):
        self.assertIsNotNone(self.uzbek.getSynSetWithId("TUR10-0000040"))

    def test_GetSynSetWithLiteral(self):
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("sıradaki", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("Türkçesi", 2))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("tropikal orman", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("mesut olmak", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("acı badem kurabiyesi", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("açık kapı siyaseti", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("bir baştan bir başa", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("eş zamanlı dil bilimi", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("bir iğne bir iplik olmak", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("yedi kat yerin dibine geçmek", 2))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("kedi gibi dört ayak üzerine düşmek", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("bir kulağından girip öbür kulağından çıkmak", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("anasından emdiği süt burnundan fitil fitil gelmek", 1))
        self.assertIsNotNone(self.uzbek.getSynSetWithLiteral("bir ayak üstünde kırk yalanın belini bükmek", 1))
        print(self.uzbek.getSynSetWithLiteral("bir ayak üstünde kırk yalanın belini bükmek", 1))
        print(self.uzbek.getSynSetWithLiteral("abakus", 2))

    def test_NumberOfSynSetsWithLiteral(self):
        self.assertEquals(1, self.uzbek.numberOfSynSetsWithLiteral("yolcu etmek"))
        self.assertEquals(2, self.uzbek.numberOfSynSetsWithLiteral("açık pembe"))
        self.assertEquals(3, self.uzbek.numberOfSynSetsWithLiteral("bürokrasi"))
        self.assertEquals(4, self.uzbek.numberOfSynSetsWithLiteral("bordür"))
        self.assertEquals(5, self.uzbek.numberOfSynSetsWithLiteral("duygulanım"))
        self.assertEquals(6, self.uzbek.numberOfSynSetsWithLiteral("sarsıntı"))
        self.assertEquals(7, self.uzbek.numberOfSynSetsWithLiteral("kuvvetli"))
        self.assertEquals(8, self.uzbek.numberOfSynSetsWithLiteral("merkez"))
        self.assertEquals(9, self.uzbek.numberOfSynSetsWithLiteral("yüksek"))
        self.assertEquals(10, self.uzbek.numberOfSynSetsWithLiteral("biçim"))
        self.assertEquals(11, self.uzbek.numberOfSynSetsWithLiteral("yurt"))
        self.assertEquals(12, self.uzbek.numberOfSynSetsWithLiteral("iğne"))
        self.assertEquals(13, self.uzbek.numberOfSynSetsWithLiteral("kol"))
        self.assertEquals(14, self.uzbek.numberOfSynSetsWithLiteral("alem"))
        self.assertEquals(15, self.uzbek.numberOfSynSetsWithLiteral("taban"))
        self.assertEquals(16, self.uzbek.numberOfSynSetsWithLiteral("yer"))
        self.assertEquals(17, self.uzbek.numberOfSynSetsWithLiteral("ağır"))
        self.assertEquals(18, self.uzbek.numberOfSynSetsWithLiteral("iş"))
        self.assertEquals(19, self.uzbek.numberOfSynSetsWithLiteral("dökmek"))
        self.assertEquals(20, self.uzbek.numberOfSynSetsWithLiteral("kaldırmak"))
        self.assertEquals(21, self.uzbek.numberOfSynSetsWithLiteral("girmek"))
        self.assertEquals(22, self.uzbek.numberOfSynSetsWithLiteral("gitmek"))
        self.assertEquals(23, self.uzbek.numberOfSynSetsWithLiteral("vermek"))
        self.assertEquals(24, self.uzbek.numberOfSynSetsWithLiteral("olmak"))
        self.assertEquals(25, self.uzbek.numberOfSynSetsWithLiteral("bırakmak"))
        self.assertEquals(26, self.uzbek.numberOfSynSetsWithLiteral("çıkarmak"))
        self.assertEquals(27, self.uzbek.numberOfSynSetsWithLiteral("kesmek"))
        self.assertEquals(28, self.uzbek.numberOfSynSetsWithLiteral("açmak"))
        self.assertEquals(33, self.uzbek.numberOfSynSetsWithLiteral("düşmek"))
        self.assertEquals(38, self.uzbek.numberOfSynSetsWithLiteral("atmak"))
        self.assertEquals(39, self.uzbek.numberOfSynSetsWithLiteral("geçmek"))
        self.assertEquals(44, self.uzbek.numberOfSynSetsWithLiteral("çekmek"))
        self.assertEquals(51, self.uzbek.numberOfSynSetsWithLiteral("tutmak"))
        self.assertEquals(59, self.uzbek.numberOfSynSetsWithLiteral("çıkmak"))

    def test_GetSynSetsWithPartOfSpeech(self):
        self.assertEquals(44074, len(self.uzbek.getSynSetsWithPartOfSpeech(Pos.NOUN)))
        self.assertEquals(17791, len(self.uzbek.getSynSetsWithPartOfSpeech(Pos.VERB)))
        self.assertEquals(12416, len(self.uzbek.getSynSetsWithPartOfSpeech(Pos.ADJECTIVE)))
        self.assertEquals(2550, len(self.uzbek.getSynSetsWithPartOfSpeech(Pos.ADVERB)))
        self.assertEquals(342, len(self.uzbek.getSynSetsWithPartOfSpeech(Pos.INTERJECTION)))
        self.assertEquals(68, len(self.uzbek.getSynSetsWithPartOfSpeech(Pos.PRONOUN)))
        self.assertEquals(60, len(self.uzbek.getSynSetsWithPartOfSpeech(Pos.CONJUNCTION)))
        self.assertEquals(29, len(self.uzbek.getSynSetsWithPartOfSpeech(Pos.PREPOSITION)))

    def test_GetLiteralsWithPossibleModifiedLiteral(self):
        english = WordNet("../english_wordnet_version_31.xml", "../english_exception.xml")
        self.assertTrue("go" in english.getLiteralsWithPossibleModifiedLiteral("went"))
        self.assertTrue("go" in english.getLiteralsWithPossibleModifiedLiteral("going"))
        self.assertTrue("go" in english.getLiteralsWithPossibleModifiedLiteral("gone"))
        self.assertTrue("be" in english.getLiteralsWithPossibleModifiedLiteral("was"))
        self.assertTrue("be" in english.getLiteralsWithPossibleModifiedLiteral("were"))
        self.assertTrue("be" in english.getLiteralsWithPossibleModifiedLiteral("been"))
        self.assertTrue("have" in english.getLiteralsWithPossibleModifiedLiteral("had"))
        self.assertTrue("play" in english.getLiteralsWithPossibleModifiedLiteral("played"))
        self.assertTrue("play" in english.getLiteralsWithPossibleModifiedLiteral("plays"))
        self.assertTrue("orange" in english.getLiteralsWithPossibleModifiedLiteral("oranges"))
        self.assertTrue("good" in english.getLiteralsWithPossibleModifiedLiteral("better"))
        self.assertTrue("well" in english.getLiteralsWithPossibleModifiedLiteral("better"))
        self.assertTrue("good" in english.getLiteralsWithPossibleModifiedLiteral("best"))
        self.assertTrue("well" in english.getLiteralsWithPossibleModifiedLiteral("best"))
        self.assertTrue("bad" in english.getLiteralsWithPossibleModifiedLiteral("worse"))
        self.assertTrue("bad" in english.getLiteralsWithPossibleModifiedLiteral("worst"))
        self.assertTrue("ugly" in english.getLiteralsWithPossibleModifiedLiteral("uglier"))
        self.assertTrue("ugly" in english.getLiteralsWithPossibleModifiedLiteral("ugliest"))
        self.assertTrue("bus" in english.getLiteralsWithPossibleModifiedLiteral("buses"))
        self.assertTrue("fly" in english.getLiteralsWithPossibleModifiedLiteral("flies"))
        self.assertTrue("leaf" in english.getLiteralsWithPossibleModifiedLiteral("leaves"))

    def test_GetInterlingual(self):
        self.assertEquals(1, len(self.uzbek.getInterlingual("ENG31-05674544-n")))
        self.assertEquals(2, len(self.uzbek.getInterlingual("ENG31-00220161-r")))
        self.assertEquals(3, len(self.uzbek.getInterlingual("ENG31-02294200-v")))
        self.assertEquals(4, len(self.uzbek.getInterlingual("ENG31-06205574-n")))
        self.assertEquals(5, len(self.uzbek.getInterlingual("ENG31-02687605-v")))
        self.assertEquals(6, len(self.uzbek.getInterlingual("ENG31-01099197-n")))
        self.assertEquals(7, len(self.uzbek.getInterlingual("ENG31-00587299-n")))
        self.assertEquals(9, len(self.uzbek.getInterlingual("ENG31-02214901-v")))
        self.assertEquals(10, len(self.uzbek.getInterlingual("ENG31-02733337-v")))
        self.assertEquals(19, len(self.uzbek.getInterlingual("ENG31-00149403-v")))

    def test_Size(self):
        self.assertEquals(77330, self.uzbek.size())

    def test_FindPathToRoot(self):
        self.assertEquals(1, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0814560"))))
        self.assertEquals(2, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0755370"))))
        self.assertEquals(3, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0516010"))))
        self.assertEquals(4, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0012910"))))
        self.assertEquals(5, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0046370"))))
        self.assertEquals(6, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0186560"))))
        self.assertEquals(7, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0172740"))))
        self.assertEquals(8, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0195110"))))
        self.assertEquals(9, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0285060"))))
        self.assertEquals(10, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0066050"))))
        self.assertEquals(11, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0226380"))))
        self.assertEquals(12, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0490230"))))
        self.assertEquals(13, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-1198750"))))
        self.assertEquals(14, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0412120"))))
        self.assertEquals(15, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-1116690"))))
        self.assertEquals(13, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0621870"))))
        self.assertEquals(14, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0822980"))))
        self.assertEquals(15, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0178450"))))
        self.assertEquals(16, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0600460"))))
        self.assertEquals(17, len(self.uzbek.findPathToRoot(self.uzbek.getSynSetWithId("TUR10-0656390"))))


if __name__ == '__main__':
    unittest.main()
