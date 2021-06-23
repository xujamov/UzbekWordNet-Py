import telebot

from WordNet.WordNet import WordNet

API_TOKEN = '1858822529:AAH29byfrRRfj-UZJi5FUz25edVeP_Uhuv8'
bot = telebot.TeleBot(API_TOKEN)
uzbek: WordNet
# uzbek = WordNet("wordnet_adj_uzb.xml")
uzbek = WordNet("word_suv_relations.xml")


def getSynonymList(text):
    for synSet in uzbek.synSetList():
        my_text = ''
        found = False

        for i in range(synSet.getSynonym().literalSize()):
            literal = synSet.getSynonym().getLiteral(i)
            my_text += f'{i + 1}: {literal.getName()}; '
            if literal and text in literal.getName():
                found = True
        if found:
            return f'Sinonimlar: {my_text}'
    return 'Sinonimlar topilmadi.'


def getRelationList(text):
    for synSet in uzbek.synSetList():
        print('---------------')
        if synSet.getSynonym().literalSize() != 0:
            print(synSet.getId(), synSet.getSynonym().getLiteral(0))
        for i in range(synSet.relationSize()):
            relation = synSet.getRelation(i)
            print(relation, getSynonymsBySynSet(uzbek.getSynSetWithId(relation.getName())))
    return 'Relations topilmadi.'


def getSynonymsBySynSet(synSet):
    if synSet is not None:
        my_text = ''
        for i in range(synSet.getSynonym().literalSize()):
            literal = synSet.getSynonym().getLiteral(i)
            my_text += f'{i + 1}: {literal.getName()}; '
        return f' {my_text}'
    else:
        return 'Relation topilmadi.'


def getAllMeanings(text):
    my_text = ''
    cnt = 1
    for meaning in uzbek.getSynSetsWithLiteral(text):
        my_text += f'{cnt}: {meaning}; '
        cnt += 1
    if my_text != '':
        return my_text
    return 'definition topilmadi'


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    request = message.text.lower()

    text = getSynonymList(request)
    meaning = getAllMeanings(request)
    relation = getRelationList(request)
    if text:
        bot.reply_to(message, text)
    if meaning:
        bot.reply_to(message, meaning)
    if relation:
        bot.reply_to(message, relation)


if __name__ == '__main__':
    text = input()
    print(getRelationList(text))

bot.polling()
