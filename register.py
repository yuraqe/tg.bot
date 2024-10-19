import json
from math import lgamma
import sqlite3
import telebot
from telebot import types


name = None
bot = telebot.TeleBot('7713433364:AAFT9GLnpec9JxIpbaMAcneLUMVmrcns4Iw')




@bot.message_handler(commands=['start'])
def start(message):
    """ Подключение к базе данных"""
    connection = sqlite3.connect('itproger.sql')    # подключение к файлу
    cur = connection.cursor()    # создаём курсор

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')    # создаём если ещё не создано
    connection.commit()
    cur.close()
    connection.close()

    bot.send_message(message.chat.id, 'Введите ваша имя, для регистрации')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    connection = sqlite3.connect('itproger.sql')
    cur = connection.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES (?, ?)", (name, password))   # вставляет ф.и в базу данных
    connection.commit()
    cur.close()
    connection.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Успешно зарегистрировано!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    connection = sqlite3.connect('itproger.sql')
    cur = connection.cursor()

    cur.execute('SELECT * FROM users')
    user = cur.fetchall()

    info = '\n'.join([f"Имя: {el[1]}, пароль: {el[2]}" for el in user])

    cur.close()
    connection.close()

    bot.send_message(call.message.chat.id, info)

if __name__ == '__main__':
    bot.polling(non_stop=True)