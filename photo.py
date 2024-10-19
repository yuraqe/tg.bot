import telebot
from telebot import types

bot = telebot.TeleBot('7713433364:AAFT9GLnpec9JxIpbaMAcneLUMVmrcns4Iw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить фото')
    markup.row(btn2, btn3)
    file = open('./photo1.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, 'privet', reply_markup=markup)
    #bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'website is opened')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, "foto delited")

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить фото', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'какое красивое фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.send_message(callback.message.chat.id, callback.message.message.id - 1)
    elif callback.data == 'edit':
        bot.send_message('edit text', callback.message.chat.id, callback.message.message_id)


if __name__ == '__main__':
    bot.polling(non_stop=True)
