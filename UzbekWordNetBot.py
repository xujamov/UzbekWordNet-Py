import telebot

from WordNet.WordNet import WordNet

API_TOKEN = '1858822529:AAH29byfrRRfj-UZJi5FUz25edVeP_Uhuv8'
bot = telebot.TeleBot(API_TOKEN)


def answer(text):
    uzbek: WordNet
    uzbek = WordNet("wordnet_adj_uzb.xml")

    return uzbek.getSynSetWithLiteral(text, 1)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    request = message.text.lower()

    text = answer(request)
    if text:
        print(text)
        bot.reply_to(message, text)


bot.polling()
