# -*- coding: utf-8 -*-

import telebot
from secret import TOKEN
# import func
from func import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, HELP)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.reply_to(message, benny_hill_this(message.text))


if __name__ == "__main__":
    bot.polling(none_stop=True)
