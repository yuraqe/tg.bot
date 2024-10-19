import json
import requests
import telebot
from telebot import types


API = 'b6c87fa3b62a4141739b031ced05a840'
bot = telebot.TeleBot('7713433364:AAFT9GLnpec9JxIpbaMAcneLUMVmrcns4Iw')

@bot.message_handler(commands=['weather'])
def start_weather_search(message):
    '''Запрос погоды!'''
    bot.send_message(message.chat.id, 'Напиши название города, в котором хочешь узнать погоду')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp} °C')

        image = 'photo.jpg' if (temp > 8.0) else 'photo1.jpg'
        with open(image, 'rb') as file:
            bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Ошибка: не удалось получить данные о погоде. Проверьте правильность названия города.')


if __name__ == '__main__':
    bot.polling(non_stop=True)
