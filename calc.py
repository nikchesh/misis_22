import telebot
from telebot import types

bot = telebot.TeleBot('')

expr = ''

keyboard = types.InlineKeyboardMarkup()

keyboard.row(
    types.InlineKeyboardButton(text = '(', callback_data='('),
    types.InlineKeyboardButton(text = ')', callback_data=')'),
    types.InlineKeyboardButton(text='^', callback_data='^'),
    types.InlineKeyboardButton(text = 'Del', callback_data='Del')

)
keyboard.row(
    types.InlineKeyboardButton(text = '7', callback_data='7'),
    types.InlineKeyboardButton(text = '8', callback_data='8'),
    types.InlineKeyboardButton(text = '9', callback_data='9'),
    types.InlineKeyboardButton(text = '/', callback_data='/')
)
keyboard.row(
    types.InlineKeyboardButton(text = '4', callback_data='4'),
    types.InlineKeyboardButton(text = '5', callback_data='5'),
    types.InlineKeyboardButton(text = '6', callback_data='6'),
    types.InlineKeyboardButton(text = '*', callback_data='*')
)
keyboard.row(
    types.InlineKeyboardButton(text = '1', callback_data='1'),
    types.InlineKeyboardButton(text = '2', callback_data='2'),
    types.InlineKeyboardButton(text = '3', callback_data='3'),
    types.InlineKeyboardButton(text = '-', callback_data='-')
)
keyboard.row(
    types.InlineKeyboardButton(text = '0', callback_data='0'),
    types.InlineKeyboardButton(text = '.', callback_data='.'),
    types.InlineKeyboardButton(text = '=', callback_data='='),
    types.InlineKeyboardButton(text = '+', callback_data='+')
)

@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'Привет! Напиши мне какое-нибудь математическое выражение, а я постараюсь его посчитать')


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global expr
    data = query.data
    if data == 'Del':
        expr = ''
    elif data == "^":
        expr+= "**"
    elif data == '=':
        try:
            expr = str(eval(expr))
        except:
            expr = 'Что-то пошло не так'

    else:
        expr+=data


    if expr == '':
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = '0', reply_markup=keyboard)
    else:
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=expr, reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)