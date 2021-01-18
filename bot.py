import pyowm
import telebot
from config import *

bot = telebot.TeleBot(TOKEN)

owm = pyowm.OWM(TOKEN_owm)

@bot.message_handler(commands=['start'])
def SayHello(message):
    bot.send_message(message.chat.id, 'Привет, {0.first_name}. Я - {1.first_name}. Бот, предназначеный для выдачи погоды. Просто введи название города, и я выдам тебе погоду! '.format(message.from_user ,bot.get_me()))



@bot.message_handler(content_types=['text'])
def get_w(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text) #Местоположение для вывода погоды
    w = observation.weather #Запрос погоды
    status = w.status #запрос статуса погоды
    temp = w.temperature('celsius')['temp'] #запрос текущей температуры
    str_temp = str(round(temp))+ '°C' #переменная температуры
    bot.send_message(message.chat.id, f'Погода в городе {message.text} равна {str_temp}.\n Статус: {status}')


bot.polling(none_stop=True)