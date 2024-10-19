import json
import webbrowser
from math import lgamma
import telebot
from telebot import types


bot = telebot.TeleBot('7713433364:AAFT9GLnpec9JxIpbaMAcneLUMVmrcns4Iw')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    pass
    #webbrowser.open('url')


@bot.message_handler(commands=['hello'])   # команды работаю через /
def main(message):
    bot.send_message(message.chat.id, f'privet, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b>, <em><u>information</u>...</em>', parse_mode='html')


@bot.message_handler()      # простые сообщения
def _info(get_massage):
    '''Должен находится в конце т.к принимает на себя весь инпут, о блоки коды с командами не будут выполнены. '''

    if get_massage.text.lower() == 'privet':
        bot.send_message(get_massage.chat.id, f'privet, {get_massage.from_user.first_name}')   #   просто выводит сообщения если слово совподают.
    elif get_massage.text.lower() == 'id':
        bot.reply_to(get_massage, f"id: {get_massage.from_user.id}")    # отвечает на сообщения

if __name__ == '__main__':
    bot.polling(non_stop=True)