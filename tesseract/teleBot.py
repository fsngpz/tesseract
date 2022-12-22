import telebot
from telebot import *
from ocr import getNotAngka
from compileMusicTabs import compile
API_TOKEN = "5757460719:AAH0Mtmn_VD532dVWLYt7jZ3REot02RNju4"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def initial_start(message):
    name = message.chat.first_name
    bot.send_message(message.from_user.id, "Hi {}, Welcome to my bot. This bot will help you to convert a picture of music tabs to sound".format(name))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.from_user.id,'''
This bot is to converting music tabs to sound.

How to use this bot?

➡️➡️First, send your picture of music tabs to this bot.
➡️➡️wait for a couple second
➡️➡️this bot will send you sound of converted picture music tabs.''')

@bot.message_handler(content_types= ["photo"])
def get_photo(message):
    userId = message.chat.id

    bot.reply_to(message, "Thank you for using me, please wait a second... I will convert the picture of music tabs to the sound")

    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    base_sound_path = r"C:\Users\User\PycharmProjects\tesseract\piano\sound"
    pict_path = fr"C:\Users\User\PycharmProjects\tesseract\tesseract\misc\picture\{fileID}.jpg"
    result_sound_path = fr"C:\Users\User\PycharmProjects\tesseract\tesseract\misc\sound\{fileID}.wav"

    with open(pict_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = getNotAngka(pict_path)

    predicted_sound = []
    for x in result:
        predicted_sound.append(f"{base_sound_path}\{x}.wav")
    compile(predicted_sound, result_sound_path)
    bot.send_message(userId, "Here is the result of your music tabs")
    bot.send_audio(message.chat.id, open(result_sound_path, 'rb'))
    bot.reply_to(message, 'Thank you for using this bot!')

bot.polling(none_stop=True) 