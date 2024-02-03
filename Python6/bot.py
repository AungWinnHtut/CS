# pip install pyTelegramBotAPI
# PythonMyanmar_bot
import random
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
API_TOKEN = '6744368147:AAFYAhA0tG5Nhsdq5cn7P3mtaK1UaxGReO0'
user_input = ""
digit = 0
count = 0
menulevel = 0
bot = telebot.TeleBot(API_TOKEN)

start_kb = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
start_kb.row('2 numbers', '3 numbers', '4 numbers')
start_kb.row('2 numbers', '3 numbers', '/start')



@bot.message_handler(commands=['start']) #/start
def start(message):   
    bot.reply_to(message, "enter digits (1,2,3,4,etc...)", reply_markup=start_kb)
  
    



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def online_class(message):
    global menulevel
    global digit
    user_input = message.text    
    match(user_input):
        case '2 numbers': 
            if menulevel ==0 :
                menulevel+=1            
                digit = 1            
                n1 = 9
                bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
                bot.reply_to(message, "How many numbers to add/ substract?")
        case '3 numbers': 
            if menulevel ==0 :
                menulevel+=1  
                digit = 2
                n1 = 99
                bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
                bot.reply_to(message, "How many numbers to add/ substract?")
        case '4 numbers':
            if menulevel ==0 :
                menulevel+=1   
                digit = 3
                n1 = 999
                bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
                bot.reply_to(message, "How many numbers to add/ substract?")
        case '2': 
            if menulevel ==1 :
                menulevel+=1 
                bot.reply_to(message, "2")
                bot.reply_to(message, "digit is " + str(digit))
                match(digit):
                    case 1: 
                        num1 = random.randint(-9,9)     
                        num2 = random.randint(-9,9)               
                        bot.reply_to(message, f"{num1} + {num2} = ?")
                    case 2:
                        num1 = random.randint(10,99)     
                        num2 = random.randint(10,99)   
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num1 = num1 * -1
                        if(s2==1):
                            num2 = num2 * -1         
                        bot.reply_to(message, f"{num1} + {num2} = ?")
                    case 3:
                        num1 = random.randint(100,999)     
                        num2 = random.randint(100,999)   
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num1 = num1 * -1
                        if(s2==1):
                            num2 = num2 * -1         
                        bot.reply_to(message, f"{num1} + {num2} = ?")
        case '3':
            if menulevel ==1 :
                menulevel+=1  
                match(digit):
                    case 1:                    
                        bot.reply_to(message, "1 + 1 + 1= ?")
                    case 2:
                        bot.reply_to(message, "11 + 11 + 11= ?")
                    case 3:
                        bot.reply_to(message, "111 + 111 + 111= ?")
        case '4': 
            if menulevel ==1 :
                menulevel+=1 
                match(digit):
                    case 1:                    
                        bot.reply_to(message, "1 + 1 + 1 + 1= ?")
                    case 2:
                        bot.reply_to(message, "11 + 11 + 11 + 11 = ?")
                    case 3:
                        bot.reply_to(message, "111 + 111 + 111+ 111= ?") 

   


bot.infinity_polling()