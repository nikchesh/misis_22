import telebot
from collections import Counter
import re

bot = telebot.TeleBot('')

def countSentences(text):
    dropEllipsisText = text.replace("...", ".")
    updateText = re.sub(r'[.!?]\s', r'~', dropEllipsisText)
    number = len(updateText.split('~'))
    return number

def popularWords(listAllWords):
    cleanWords = []

    dropList = ['без' , 'в' , 'до' , 'для' , 'за' , 'из' , 'к' , 'на' , 'над' , 'о' , 'об' , 'от' , 'по' , 'под' , 'пред ,' 'при' , 'про' , 'с' , 'у' , 'через',
               'а', 'и', 'чтобы' , 'если',
               'но', 'или', 'либо', 'что', 'хотя', 'будто', 'ли']

    print(type(dropList))
    for word in listAllWords:
        if word.lower() not in dropList:
            cleanWords += [(word.lower(), )]
    print(cleanWords)

    res = []
    temp = set()
    maxCount = 0
    maxCountWords = []
    counter = Counter(cleanWords)
    for sub in cleanWords:
        if sub not in temp:
            res.append((counter[sub],) + sub)
            temp.add(sub)

    for t in res:
        if (t[0] > maxCount):
            maxCount = t[0]
            maxCountWords = [t[1]]
        elif (t[0] == maxCount):
            maxCountWords.append(t[1])

    return maxCountWords


def findMaxWord(listWords):
    maxWord = ""
    for word in listWords:
        if (len(word) > len(maxWord)):
            maxWord = word
    return maxWord




def analizeText(text):
    #длина текста
    length = len(text)
    #Количество предложений
    countSent = countSentences(text)

    reg = re.compile('[^а-яА-Яё ]')
    cleanLine = reg.sub('', text)
    listWords = cleanLine.split(" ")
  #  listAllWordsT = []
    listAllWords = []

    for word in listWords:
        if (word != ''):
#            listAllWordsT += [(word, )]
            listAllWords.append(word)


    #Самые популярные слова
    popularWordsList = popularWords(listAllWords)

    #Количество уникальных слов
    distinctWordsCount = len(set(listWords))

    #Самое длинное слово
    maxWord = findMaxWord(listAllWords)


    return length,countSent,distinctWordsCount,popularWordsList,maxWord



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Пришли мне текст, а я выведу информацию о нем')




@bot.message_handler(content_types=["text"])
def handle_text(message):
        initText = message.text
        textLength, numberOfSentences,uniqueCount, popularWordsList,maxWord= analizeText(initText)
        bot.send_message(message.chat.id, f'Длина текста: {textLength}\nКоличество предложений: {numberOfSentences}\nЧисло уникальных слов: {uniqueCount}\nСамые популярные слова: {popularWordsList}\nСамое длинное слово: {maxWord}')






bot.polling(none_stop=True, interval=0)