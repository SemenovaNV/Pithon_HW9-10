import json
import requests
from pprint import pprint
import datetime
from telegram.ext import Updater, CommandHandler

updater = Updater('5862320588:AAGx_C7GXq7db_Dz4yXnbb8RrwufFzdkLw4')
token_weather = '41c4d74afd3054cd442f9199c10eefe6'

def Get_weather(city, token_weather):
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric")
        data = r.json()
        pprint(data)

        city = data["name"] 
        cur_weather = data["main"]["temp"] 
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        return ((f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                f"Погода в городе: {city}\nТемпература: {cur_weather}C°\n"
                f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                f"Прекрасного дня!"))

    except Exception as ex:
        # print(ex)
        return "Проверьте название города"            

def main():
    city = input("Введите город: ")
    print(Get_weather(city, token_weather()))

# if __name__ == '__main__':
#     main()

