import telegram
import json
import requests as req
from telegram import Update 
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
import datetime
from main import Get_weather, token_weather
from spy import *

updater = Updater('5862320588:AAGx_C7GXq7db_Dz4yXnbb8RrwufFzdkLw4', use_context=True)
dispatcher = updater.dispatcher

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/city')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def weather_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    city = items[1]
    update.message.reply_text(f'{Get_weather(city, token_weather)}')

def calc_rac_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    x = float(items[1])
    action = items[2]
    y = float(items[3])
    if action == '+':
        update.message.reply_text(f'{x} {action} {y} = {x + y}')
    elif action == '-':
        update.message.reply_text(f'{x} {action} {y} = {x - y}')
    elif action == '*':
        update.message.reply_text(f'{x} {action} {y} = {x * y}')
    elif action == '/':
        update.message.reply_text(f'{x} {action} {y} = {x / y}')

def calc_compl_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() 
    x = complex(items[1])
    action = items[2]
    y = complex(items[3])
    if action == '+':
        update.message.reply_text(f'{x} {action} {y} = {x + y}')
    elif action == '-':
        update.message.reply_text(f'{x} {action} {y} = {x - y}')
    elif action == '*':
        update.message.reply_text(f'{x} {action} {y} = {x * y}')
    elif action == '/':
        update.message.reply_text(f'{x} {action} {y} = {x / y}')




# обработка команды старт (создаем Inline клавиатуру)
def startCommand(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('Поздороваться', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('Помощь', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('Отразить текущее время', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('Прогноз погоды', callback_data='buttonD')
    buttonE = telegram.InlineKeyboardButton('Калькулятор рациональных чисел', callback_data='buttonE')
    buttonF = telegram.InlineKeyboardButton('Калькулятор комплексных чисел', callback_data='buttonF')
    markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD], [buttonE], [buttonF]])

    update.message.reply_text('Привет! Я готов к работе, выберите одно из возможных действий',reply_markup=markup)
    return callback

# обработка нажатия клавиш клавиатуры
def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Хотите поздороваться? Введите /hi')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Для отображения выполняемых операций введите /help')

    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Для отображения текущего времени введите /time')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Для отображения прогноза погоды в интересующем городе введите /city "Город"')

    if variant == 'buttonE':
        query.answer()
        query.edit_message_text(text='Для выполнения арифметической операции введите /calc_rac "x + y"')

    if variant == 'buttonF':
        query.answer()
        query.edit_message_text(text='Для выполнения арифметической операции введите /calc_compl "x + y"')


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
hi_handler = MessageHandler(Filters.regex('Привет'), hi_command)
help_handler = MessageHandler(Filters.regex('Помощь: '), help_command)
time_handler = MessageHandler(Filters.regex('Время: '), time_command)
weather_handler = MessageHandler(Filters.regex('Прогноз погоды: '), weather_command)
calc_rac_handler = MessageHandler(Filters.regex('Калькулятор рациональных чисел: '), calc_rac_command)
calc_compl_handler = MessageHandler(Filters.regex('Калькулятор комплексных чисел: '), calc_compl_command)
callback_button_handler = CallbackQueryHandler(callback=callback, pattern=None, run_async=False)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(hi_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(time_handler)
dispatcher.add_handler(weather_handler)
dispatcher.add_handler(calc_rac_handler)
dispatcher.add_handler(calc_compl_handler)
dispatcher.add_handler(callback_button_handler)

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('city', weather_command))
updater.dispatcher.add_handler(CommandHandler('calc_rac', calc_rac_command))
updater.dispatcher.add_handler(CommandHandler('calc_compl', calc_compl_command))

print('server start')
updater.start_polling()
updater.idle()