import os
from flask import Flask, request
from telebot import types
from pyowm import OWM
from pyowm.utils.config import get_default_config
import telebot

TOKEN = '5262735741:AAHL1PTf8GnPWXCFlgNp1Dngrei-RynBzB4'

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

d = {"second_1": "sword_demon.jpg", "second_2": "anime-rain-cyber.jpg", "second_3": "wallpaperflare.com_wallpaper (1).jpg", "second_4": "sword_demon_purple.jpg", "second_5": "anime girl.jpg", "second_6": "space1.jpg",
    "second_7": "wallpaperflare.com_wallpaper (3).jpg", "second_8": "space2.jpg", "second_9": "planet_brake.jpg", "second_10": "little_princ.jpg",
    "second_11": "nature1.jpg", "second_12": "nature2.jpg", "second_13": "nature3.jpg", "second_14": "nature4.jpg", "second_15": "nature5.jpg", } 
rand = ["anime-rain-cyber.jpg","space1.jpg", "anime girl.jpg", "wallpaperflare.com_wallpaper (1).jpg", "space2.jpg", 'nature1.jpg', 'nature2.jpg',
'nature3.jpg', 'nature4.jpg', 'nature5.jpg', 'planet_brake.jpg', 'wallpaperflare.com_wallpaper (3).jpg', 'sword_demon.jpg', 'sword_demon.jpg', 'little_princ.jpg']

@bot.message_handler(commands=['Photos'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Аниме', callback_data='first_1')
    button2 = types.InlineKeyboardButton(text='Космос', callback_data='first_2')
    button3 = types.InlineKeyboardButton(text='Природа', callback_data='first_3')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.send_message(message.chat.id, text="Выбери тематику фото", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('first'))
def photos1(call):
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == 'first_1':
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Фото 1', callback_data='second_1')
        button2 = types.InlineKeyboardButton(text='Фото 2', callback_data='second_2')
        button3 = types.InlineKeyboardButton(text='Фото 3', callback_data='second_3')
        button4 = types.InlineKeyboardButton(text='Фото 4', callback_data='second_4')
        button5 = types.InlineKeyboardButton(text='Фото 5', callback_data='second_5')
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(button4)
        keyboard.add(button5)
        bot.send_message(call.message.chat.id, text="Выбери фото (Аниме)", reply_markup=keyboard)
    elif call.data == 'first_2':
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Фото 1', callback_data='second_6')
        button2 = types.InlineKeyboardButton(text='Фото 2', callback_data='second_7')
        button3 = types.InlineKeyboardButton(text='Фото 3', callback_data='second_8')
        button4 = types.InlineKeyboardButton(text='Фото 4', callback_data='second_9')
        button5 = types.InlineKeyboardButton(text='Фото 5', callback_data='second_10')
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(button4)
        keyboard.add(button5)
        bot.send_message(call.message.chat.id, text="Выбери фото (Космос)", reply_markup=keyboard)
    elif call.data == 'first_3':
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Фото 1', callback_data='second_11')
        button2 = types.InlineKeyboardButton(text='Фото 2', callback_data='second_12')
        button3 = types.InlineKeyboardButton(text='Фото 3', callback_data='second_13')
        button4 = types.InlineKeyboardButton(text='Фото 4', callback_data='second_14')
        button5 = types.InlineKeyboardButton(text='Фото 5', callback_data='second_15')
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        keyboard.add(button4)
        keyboard.add(button5)
        bot.send_message(call.message.chat.id, text="Выбери фото (Природа)", reply_markup=keyboard)

amount = 0
photo_id = 0

@bot.callback_query_handler(func=lambda call: call.data.startswith('second'))
def photos2(call):
    bot.answer_callback_query(callback_query_id=call.id)
    global amount
    global rand
    global photo_id
    if amount > 0:
        bot.delete_message(call.message.chat.id, photo_id)
    amount +=1
    img = open(d[call.data], "rb")
    photo_id =bot.send_photo(call.message.chat.id, img).message_id
    img.close()
    rand = d.values()

place = ''
@bot.message_handler(commands=['Weather'])
def get_weather(message):
    bot.send_message(message.from_user.id, 'Введи название города')
    bot.register_next_step_handler(message, in_which_town)
def in_which_town(message):
    global place
    place = str(message.text)
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('1af6d94aef9fadbb7f4fa20c8cdbb9a9', config_dict)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    weather = observation.weather

    temp = weather.temperature("celsius")
    temp_now = temp['temp']
    temp_feels = temp['feels_like']
    wind = weather.wind()['speed']
    status = weather.detailed_status

    bot.send_message(message.chat.id, "В городе " + str(place).capitalize() + " температура " + str(round(temp_now)) + "°C" + "\n" + 
        "Ощущается как " + str(round(temp_feels)) + "°C" + "\n" +
        "Скорость ветра " + str(round(wind)) + " м/с" + "\n" + 
        "Описание: " + str(status))

@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == '/start':
        stik = open('Илон и шампусико.webp', 'rb')
        bot.send_sticker(message.chat.id, stik)
        bot.send_message(message.chat.id, 'Привет, я хотя уже и не тестовый бот но всё ещё нахожусь в разработке так что если будут какие-то баги то их наверное скоро исправит мой разраб, но лучше напиши (@HiikiToSS)\n Введи \" /commands\" чтобы увидеть список доступных команд')
        stik.close()
    elif message.text == '/Cats':
        bot.send_message(message.from_user.id, 'https://www.youtube.com/results?search_query=мемы+с+котиками')
        bot.send_message(message.from_user.id, 'мемы с котиками, как ты и хотел')
    elif message.text == '/Anime' or message.text == '/anime memes' or message.text == '/аниме':
        bot.send_message(message.from_user.id, 'https://www.youtube.com/results?search_query=аниме+приколы')
        bot.send_message(message.from_user.id, 'аниме приколы')
    elif message.text == '/commands':
        bot.send_message(message.from_user.id, '/Weather \n /Cats \n /Anime \n /Photos \n /Random_photo')
    elif message.text == '/Random_photo':
        randPhoto = random.choice(rand)
        randImg = open(randPhoto, 'rb')
        bot.send_photo(message.from_user.id, randImg)
        randImg.close()
    else:
        bot.send_message(message.from_user.id, text = "Я ещё не нейронка чтобы отвечать на любые вопросы, введи /commands чтобы увидеть список команд")
  
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://hikkibotik.herokuapp.com/' + TOKEN)
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
