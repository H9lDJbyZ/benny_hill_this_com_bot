# -*- coding: utf-8 -*-

import telebot
from secret import TOKEN

BENNY_HILL_THIS = 'bennyhillthis.com/'
YOUTUBECOM = 'youtube.com/watch'
YOUTUBE = 'youtu.be/'
HELP = 'Пришли ссылку на ютуб'

bot = telebot.TeleBot(TOKEN)


def benny_hill_this(url):
    url = url.replace('www.', '', 1)
    if YOUTUBECOM in url:
        # https://youtube.com/watch?v=SEqF-iHCblE
        # https://bennyhillthis.com/?v=SEqF-iHCblE
        url = url.replace(YOUTUBECOM, BENNY_HILL_THIS)
    elif YOUTUBE in url:
        # https://youtu.be/SEqF-iHCblE
        # https://bennyhillthis.com/?v=SEqF-iHCblE
        url = url.replace(YOUTUBE, f'{BENNY_HILL_THIS}?v=')
    else:
        url = HELP
    return url


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, HELP)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.reply_to(message, benny_hill_this(message.text))


if __name__ == "__main__":
    bot.polling(none_stop=True)
