from tarfile import TruncatedHeaderError

import  telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('7713433364:AAFT9GLnpec9JxIpbaMAcneLUMVmrcns4Iw')
currnecy = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['convert'])
def start_convert(message):
    bot.send_message(message.chat.id, 'enter the summ')
    bot.register_next_step_handler(message, summa)

def summa(message):
    ''' выводит 4 кнопки'''
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'enter the digits')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')  #С большой буквы выводится, с маленькой передаётся в callback
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'chose the pair of currency', reply_markup=markup)
    else:
        bot.reply_to(message, 'digit shoud be greater then 0')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    '''обработка при нажатия на кнопки'''
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currnecy.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'got: {round(res, 2)}. u can try again')
       # bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'enter pairs using /')
        bot.register_next_step_handler(call.message, my_cur)

def my_cur(message):
    try:
        values = message.text.upper().split('/')
        res = currnecy.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'got: {round(res, 2)}. u can try again')
        #bot.register_next_step_handler(message, summa)
    except:
        bot.send_message(message.chat.id, f"something wrong, enter the summ")
        bot.register_message_handler(message, my_cur)



if __name__ == '__main__':
    bot.polling(non_stop=True)
