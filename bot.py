import telebot
import time
from pars import parsing
from datetime import datetime
from Tok import TOKEN
bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


while True:
    chat_id = '@Subsidies81'
    t = datetime.now()
    lstdict = parsing(t)
    text = ''
    for i in lstdict:
        text = ''
        for k, v in i.items():
            text += str(k) + ' ' + str(v) + '\n'
        bot.send_message(chat_id=chat_id, text=text)
        time.sleep(1)
    bot.send_message(chat_id=chat_id, text='Sleep')
    time.sleep(14400)

bot.polling(none_stop=False, interval=10)
