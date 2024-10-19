import json
import webbrowser
from math import lgamma
import telebot
from telebot import types


name = None
bot = telebot.TeleBot('7713433364:AAFT9GLnpec9JxIpbaMAcneLUMVmrcns4Iw')


@bot.message_handler(commands=['photo'])
def start(message):
    """При вводе команды открывает меню с кнопками или отпраляет фото, видео, аудио."""
    markup = types.ReplyKeyboardMarkup()
    btm1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btm1)
    btm2 = types.KeyboardButton('Удалить фото')
    btm3 = types.KeyboardButton('Изменить текст')
    markup.row(btm2, btm3)

    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Сайт был открыт')
        #webbrowser.open('https://google.com')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'deleted')
    elif message.text == 'Изменить текст':
        bot.send_message(message.chat.id, 'Текст изменён')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    """если пользователь отпровляет фото, выводит меню функций"""
    markup_photo = types.InlineKeyboardMarkup()
    btm1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    markup_photo.row(btm1)
    btm2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btm3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup_photo.row(btm2, btm3)

    bot.reply_to(message, 'Очень красивое фото!', reply_markup=markup_photo)

@bot.callback_query_handler(func=lambda call: True)
def callback_message(callback):
    """Управления меню функций get_photo"""
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)   # удаляет предыдущие фото
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)   # к текущему фото добавляет текст.


bot.polling(non_stop=True)
#bot.infinity_polling()