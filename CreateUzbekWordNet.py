from WordNet.WordNet import WordNet

uzbek: WordNet
uzbek = WordNet("turkish_wordnet.xml")
print(1, uzbek.numberOfSynSetsWithLiteral('su'))
for elem in uzbek.getSynSetsWithLiteral('su'):
    # print(elem)

    for i in range(elem.getSynonym().literalSize()):
        literal = elem.getSynonym().getLiteral(i)
        print(literal)
    uzbek.removeSynSet(elem)
print(2, uzbek.numberOfSynSetsWithLiteral('su'))
for elem in uzbek.getSynSetsWithLiteral('su'):
    # print(elem)

    for i in range(elem.getSynonym().literalSize()):
        literal = elem.getSynonym().getLiteral(i)
        print(literal)
uzbek.saveAsXml("uzb_wordnet.xml")
# cnt = 0
# for synSet in uzbek.synSetList():
#     for i in range(synSet.getSynonym().literalSize()):
#         literal = synSet.getSynonym().getLiteral(i)
#         if cnt < 100:
#             # print(literal.setName('su'))
#             print(literal)
#         cnt += 1
#     for i in range(synSet.relationSize()):
#         relation = synSet.getRelation(i)
#         if cnt < 100:
#             print(i, synSet)
#             # print(literal.setName('su'))
#             print(relation, uzbek.getSynSetWithId(relation.getName()))
#         cnt += 1
