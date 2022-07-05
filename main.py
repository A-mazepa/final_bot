import telebot

from config import *
from extensions import Converter, ApiExeption


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Привет!'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message): #берем объект mess, обращаемся к полю text
    try:
        base, sym, amount = message.text.split()
    except ApiExeption as e:
        bot.reply_to(message, "Неверное количество параметров")

    try:
        new_price = Converter.get_price(base, sym, amount)
        bot.reply_to(message, f'Цена {amount} {base} в {sym} : {new_price}')
    except ApiExeption as e:
        bot.reply_to(message, f'Ошибка в команде: \n{e}')




bot.polling()