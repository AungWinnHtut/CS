# pip install pyTelegramBotAPI
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
API_TOKEN = '6755851932:AAHE0EP6aX7As10QF7YnDmHJB9E4dor-u7k'

bot = telebot.TeleBot(API_TOKEN)


kb_home = ReplyKeyboardMarkup(resize_keyboard=True)   
kb_home.add(KeyboardButton('online class'))
kb_home.add(KeyboardButton('school fee'))
kb_home.add(KeyboardButton('help'))


kb_language = ReplyKeyboardMarkup(resize_keyboard=True)
kb_language.add(KeyboardButton('C'))
kb_language.add(KeyboardButton('C++'))
kb_language.add(KeyboardButton('Python'))
kb_language.add(KeyboardButton('Home'))




if not (os.path.exists('start.txt') and os.path.exists('help.txt') and os.path.exists('onlineclass.txt') and os.path.exists('schoolfee.txt')and os.path.exists('contact.txt') ):
    print('There is no such file!')
    exit(1)
    
with open('start.txt','r', encoding='utf-8') as start_file:
    start_str = start_file.read()

with open('help.txt','r', encoding='utf-8') as help_file:
    help_str = help_file.read()

with open('contact.txt','r', encoding='utf-8') as contact_file:
    contact_str = contact_file.read()

with open('onlineclass.txt','r', encoding='utf-8') as onlineclass_file:
    onlineclass_str = onlineclass_file.read()

with open('schoolfee.txt','r', encoding='utf-8') as schoolfee_file:
    schoolfee_str = schoolfee_file.read()


@bot.message_handler(commands=['start']) #/start
def start(message):   
    bot.reply_to(message, start_str)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=kb_home)

@bot.message_handler(commands=['help']) #/help
def help(message):  
    bot.reply_to(message, help_str)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def online_class(message):
    if  'online class' in message.text:
        bot.send_message(message.chat.id, "Choose an Language:", reply_markup=kb_language)
    elif 'school fee' in message.text:
        bot.reply_to(message, schoolfee_str)
    elif 'Home' in message.text:
        bot.send_message(message.chat.id, "Choose an Language:", reply_markup=kb_home)
    else:
        bot.reply_to(message, contact_str)


bot.infinity_polling()