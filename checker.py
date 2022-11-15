import requests
import telebot

bot = telebot.TeleBot('')
answers = {
    400: "сервер обнаружил в запросе клиента синтаксическую ошибку",
    401: "для доступа к запрашиваемому ресурсу требуется аутентификация.",
    403: "сервер понял запрос, но он отказывается его выполнять из-за ограничений в доступе для клиента к указанному ресурсу.",
    404: " Сервер понял запрос, но не нашёл соответствующего ресурса по указанному URL.",
    200: "Все хорошо..."
}

def get_answer(r):
    global answers
    try:
        return answers[r]
    except:
        return "какая-то другая ошибка, которую я не описал"

def url_check(url):
    try:
        r = requests.head(url).status_code
        return get_answer(r)
    except:
        return  "Что-то явно пошло не так!"


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/checker':
        bot.send_message(message.from_user.id, "Пришли ссылку на сайт, а я его проверю");
        bot.register_next_step_handler(message, getStatus); #следующий шаг – функция getStatus
    else:
        bot.send_message(message.from_user.id, 'Напиши /checker');

def getStatus(site): 
    answer = url_check(site.text)
    bot.send_message(site.from_user.id, answer)


bot.polling(none_stop=True, interval=0)
