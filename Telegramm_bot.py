import os

from flask import Flask, request

import telebot

TOKEN = '5262735741:AAHL1PTf8GnPWXCFlgNp1Dngrei-RynBzB4'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)



rand = ["Rem-re-zero.jpg","wallpaperflare.com_wallpaper (1).jpg", "anime girl.jpg", "wallpaperflare.com_wallpaper (1).jpg", "wallpaperflare.com_wallpaper (4).jpg"]

@bot.message_handler(commands=['Photos'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Аниме', callback_data='first_1')
    button2 = types.InlineKeyboardButton(text='Космос', callback_data='first_2')
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_message(message.chat.id, text="Выбери тематику фото", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('first'))
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id) #text='Спасибо за честный ответ!'
    if call.data == 'first_1':
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Фото 1', callback_data='second_1')
        button2 = types.InlineKeyboardButton(text='Фото 2', callback_data='second_2')
        button3 = types.InlineKeyboardButton(text='Фото 3', callback_data='second_3')
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        bot.send_message(call.message.chat.id, text="Выбери фото (Аниме)", reply_markup=keyboard)
    elif call.data == 'first_2':
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Фото 1', callback_data='second_4')
        button2 = types.InlineKeyboardButton(text='Фото 2', callback_data='second_5')
        button3 = types.InlineKeyboardButton(text='Фото 3', callback_data='second_6')
        keyboard.add(button1)
        keyboard.add(button2)
        keyboard.add(button3)
        bot.send_message(call.message.chat.id, text="Выбери фото (Космос)", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('second'))
def query_handler1(call):
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == 'second_1':
        img = open("anime girl.jpg", "rb")
        bot.send_photo(call.message.chat.id, img)
        img.close()
    elif call.data == 'second_2':
        img = open("Rem-re-zero.jpg", "rb")
        bot.send_photo(call.message.chat.id, img)
        img.close()
    elif call.data == 'second_3':
        img = open("wallpaperflare.com_wallpaper (1).jpg", "rb")
        bot.send_photo(call.message.chat.id, img)
        img.close()
    elif call.data == 'second_4':
        img = open("wallpaperflare.com_wallpaper (3).jpg", "rb")
        bot.send_photo(call.message.chat.id, img)
        img.close()
    elif call.data == 'second_5':
        img = open("wallpaperflare.com_wallpaper (4).jpg", "rb")
        bot.send_photo(call.message.chat.id, img)
        img.close()
    elif call.data == 'second_6':
        img = open("wallpaperflare.com_wallpaper (2).jpg", "rb")
        bot.send_photo(call.message.chat.id, img)
        img.close()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        stik = open('Илон и шампусико.webp', 'rb')
        bot.send_sticker(message.chat.id, stik)
        bot.send_message(message.chat.id, 'Привет, я тестовый бот, так что если что-то не работает то это скоро исправят (наверное) \n Введи \" /commands\" чтобы увидеть список доступных команд')
        stik.close()
    elif message.text == "/Exit":
        bot.send_message(message.from_user.id, "Пока, мой дорогой друг")
    elif message.text == '/Random_numbers':
        rand0_100 = random.randint(0,100)
        bot.send_message(message.from_user.id, rand0_100)
    elif message.text == '/Cats':
        bot.send_message(message.from_user.id, 'https://www.youtube.com/results?search_query=мемы+с+котиками - мемы с котиками, как ты и хотел')
    elif message.text == '/Anime' or message.text == '/anime memes' or message.text == '/аниме':
        bot.send_message(message.from_user.id, 'https://www.youtube.com/results?search_query=аниме+приколы - аниме приколы')
    elif message.text == '/commands':
        bot.send_message(message.from_user.id, '/Random_numbers \n /Cats \n /Anime \n /Hello \n /Photos \n /Random_photo \n /Exit') #сделай ветвление после нажатия space_photos сделай 3 кнопки и пусть в них будет фото 1\2\3
    elif message.text == '/Hello' or message.text ==  '/Hello' or message.text == '/Hi' or message.text == '/hi':
        bot.send_message(message.from_user.id, 'Привет!')
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
