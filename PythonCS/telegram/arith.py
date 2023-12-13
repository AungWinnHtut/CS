# pip install pyTelegramBotAPI
# PythonMyanmar_bot
import random
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton 
import os

import time # To use Time.Sleep function.
# from telegram import Update 
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

API_TOKEN = '6399052487:AAGNP-38DgSc_Y_P8m36PZ4oZPV-4vy5afM'
user_input = ""
digit = 0
count = 0
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start']) #/start
def start(message):
    #Creating Keyboard for 1 Digit, 2 Digits and 3 Digits.
    start_kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start_kb.row('1 Digit', '2 Digits', '3 Digits')   
    bot.reply_to(message, "Welcome to KTHHMaths Rev2... \nPlease select how many digits do you want to play with!", reply_markup=start_kb)
 
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def KTHHMaths(message):
    #Creating Keyboard for 2 Numbers, 3 Numbers, 4 Numbers and 5 Numbers.
    start_kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start_kb.row('2 Numbers', '3 Numbers')
    start_kb.row('4 Numbers', '5 Numbers')
    
    global digit
    global sum
    global num121, num122, num221, num222, num321, num322
    global num131, num132, num133, num231, num232, num233, num331, num332, num333
    global num141, num142, num143, num144, num241, num242, num243, num244, num341, num342, num343, num344
    global num151, num152, num153, num154, num155, num251, num252, num253, num254, num255, num351, num352, num353, num354, num355
    

    user_input = message.text

    # Asking for how many digits to play...
    if user_input == '1 Digit': 
            digit = 1            
            n1 = 9
            bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
            bot.reply_to(message, f"How many numbers to add/ substract?" , reply_markup=start_kb)
    elif user_input == '2 Digits': 
            digit = 2
            n1 = 99
            bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
            bot.reply_to(message, f"How many numbers to add/ substract?" , reply_markup=start_kb)
    elif user_input == '3 Digits': 
            digit = 3
            n1 = 999
            bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
            bot.reply_to(message, f"How many numbers to add/ substract?" , reply_markup=start_kb)

        # Asking for how many numbers to play...
    elif user_input == '2 Numbers': # To add 2 numbers
                bot.reply_to(message, "You have selected to play with 2 numbers for adding/ substraction of digits! \nWhat is the answer for below?")
                if digit == 1: # for 1 digit calculation
                        num121 = random.randint(-9,9)     
                        num122 = random.randint(-9,9)               
                        user_input_level3 = bot.reply_to(message, f"The sum of {num121} , {num122} = ?")
                        bot.register_next_step_handler(user_input_level3, answer12)

                elif digit == 2: # for 2 digit calculation
                        num221 = random.randint(10,99)     
                        num222 = random.randint(10,99)   
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num221 = num221 * -1
                        if(s2==1):
                            num222 = num222 * -1         
                        user_input_level3 = bot.reply_to(message, f"The sum of {num221} , {num222} = ?")
                        bot.register_next_step_handler(user_input_level3,answer22)
                elif digit == 3: # for 3 digit calculation
                        num321 = random.randint(100,999)     
                        num322 = random.randint(100,999)   
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num321 = num321 * -1
                        if(s2==1):
                            num322 = num322 * -1         
                        user_input_level3 = bot.reply_to(message, f"The sum of {num321} , {num322} = ?")
                        bot.register_next_step_handler(user_input_level3,answer32)
                else:
                        # Handle the case when user_input doesn't match any of the expected values
                        bot.reply_to(message, "Invalid input! Please choose a valid option.")
                    
    elif user_input == '3 Numbers':  # To add 3 numbers
                bot.reply_to(message, "You have selected to play with 3 numbers for adding/ substraction of digits! \nWhat is the answer for below?")
                if digit ==  1: # for 1 digit calculation
                        num131 = random.randint(-9,9)     
                        num132 = random.randint(-9,9)  
                        num133 = random.randint(-9,9)              
                        user_input_level3 = bot.reply_to(message, f"The sum of {num131} , {num132} , {num133} = ?")
                        bot.register_next_step_handler(user_input_level3,answer13)
                elif digit == 2: # for 2 digit calculation
                        num231 = random.randint(10,99)     
                        num232 = random.randint(10,99)   
                        num233 = random.randint(10,99) 
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num231 = num231 * -1
                        if(s2==1):
                            num232 = num232 * -1         
                        user_input_level3 = bot.reply_to(message, f"The sum of {num231} , {num232} , {num233} = ?")
                        bot.register_next_step_handler(user_input_level3,answer23)
                elif digit == 3: # for 3 digit calculation
                        num331 = random.randint(100,999)     
                        num332 = random.randint(100,999)   
                        num333 = random.randint(100,999) 
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num331 = num331 * -1
                        if(s2==1):
                            num332 = num332 * -1         
                        user_input_level3 = bot.reply_to(message, f"The sum of {num331} , {num332} , {num333} = ?")
                        bot.register_next_step_handler(user_input_level3,answer33)
                else:
                        # Handle the case when user_input doesn't match any of the expected values
                        bot.reply_to(message, "Invalid input! Please choose a valid option.")

    elif user_input == '4 Numbers': # To add 4 numbers
                bot.reply_to(message, "You have selected to play with 4 numbers for adding/ substraction of digits! \nWhat is the answer for below?")
                if digit ==  1: # for 1 digit calculation
                        num141 = random.randint(-9,9)     
                        num142 = random.randint(-9,9)  
                        num143 = random.randint(-9,9)
                        num144 = random.randint(-9,9)              
                        user_input_level3 = bot.reply_to(message, f"The sum of {num141} , {num142} , {num143} , {num144} = ?")
                        bot.register_next_step_handler(user_input_level3,answer14)
                elif digit ==  2: # for 2 digit calculation
                        num241 = random.randint(10,99)     
                        num242 = random.randint(10,99)   
                        num243 = random.randint(10,99) 
                        num244 = random.randint(10,99)  
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num241 = num241 * -1
                        if(s2==1):
                            num242 = num242 * -1         
                        user_input_level3 = bot.reply_to(message, f"The sum of {num241} , {num242} , {num243} , {num244} = ?")
                        bot.register_next_step_handler(user_input_level3,answer24)
                elif digit ==  3: # for 3 digit calculation
                        num341 = random.randint(100,999)     
                        num342 = random.randint(100,999)   
                        num343 = random.randint(100,999) 
                        num344 = random.randint(100,999)  
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num341 = num341 * -1
                        if(s2==1):
                            num342 = num342 * -1         
                        user_input_level3 = bot.reply_to(message, f"The sum of {num341} , {num342} , {num343} , {num344} = ?")
                        bot.register_next_step_handler(user_input_level3,answer34)
                else:
                        # Handle the case when user_input doesn't match any of the expected values
                        bot.reply_to(message, "Invalid input! Please choose a valid option.")

    elif user_input == '5 Numbers': # To add 4 numbers
                bot.reply_to(message, "You have selected to play with 5 numbers for adding/ substraction of digits! \nWhat is the answer for below?")
                if digit ==  1: # for 1 digit calculation
                        num151 = random.randint(-9,9)     
                        num152 = random.randint(-9,9)  
                        num153 = random.randint(-9,9)
                        num154 = random.randint(-9,9)              
                        num155 = random.randint(-9,9)
                        user_input_level3 = bot.reply_to(message, f"The sum of {num151} , {num152} , {num153} , {num154} , {num155} = ?")
                        bot.register_next_step_handler(user_input_level3,answer15)
                elif digit ==  2: # for 2 digit calculation
                        num251 = random.randint(10,99)     
                        num252 = random.randint(10,99)   
                        num253 = random.randint(10,99) 
                        num254 = random.randint(10,99)  
                        num255 = random.randint(10,99)
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num251 = num251 * -1
                        if(s2==1):
                            num252 = num252 * -1         
                        user_input_level3 = bot.reply_to(message, f"The sum of {num251} , {num252} , {num253} , {num254} , {num255} = ?")
                        bot.register_next_step_handler(user_input_level3,answer25)
                elif digit ==  3: # for 3 digit calculation
                        num351 = random.randint(100,999)     
                        num352 = random.randint(100,999)   
                        num353 = random.randint(100,999) 
                        num354 = random.randint(100,999)  
                        num355 = random.randint(100,999)
                        s1 = random.randint(0,1)
                        s2 = random.randint(0,1)   
                        if(s1==1):
                            num351 = num351 * -1
                        if(s2==1):
                            num352 = num352 * -1         
                        user_input_level3 = bot.reply_to(message, f"The sum of {num351} , {num352} , {num353} , {num354} , {num355} = ?")
                        bot.register_next_step_handler(user_input_level3,answer35)
                else:
                        # Handle the case when user_input doesn't match any of the expected values
                        bot.reply_to(message, "Invalid input! Please choose a valid option.")
    
    else:
                # Handle the case when user_input doesn't match any of the expected values
                bot.reply_to(message, "Invalid input! Please choose a valid option.")
                bot.send_message(chat_id='1692929855',text="Start again...", reply_markup=get_start_button()) 

def answer12(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num121 + num122
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
        # time.sleep(15)
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer22(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num221 + num222
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer32(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num321 + num322
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer13(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num131 + num132 + num133
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer23(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num231 + num232 + num233
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer33(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num331 + num332 + num333
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer14(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num141 + num142 + num143 + num144
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer24(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num241 + num242 + num243 + num244
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer34(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num341 + num342 + num343 + num344
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer15(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num151 + num152 + num153 + num154 + num155
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer25(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num251 + num252 + num253 + num254 + num255
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def answer35(message):
    chat_id = message.chat.id
    user_input = message.text
    sum = num351 + num352 + num353 + num354 + num355
    if sum == int(user_input) :
        # bot.send_message(chat_id, 'You have answered {user_input}.')
        bot.send_message(chat_id, f'Great! Your answer {user_input} is correct!')
        bot.send_message(chat_id='1692929855',text="Good Job!", reply_markup=get_start_button()) 
    else:
        bot.send_message(chat_id, f'Sorry! The correct answer is {sum}!')
        bot.send_message(chat_id='1692929855',text="Please try to concentrate more...", reply_markup=get_start_button()) 

def get_start_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    start_button = types.KeyboardButton("/start")
    markup.add(start_button)
    return markup
bot.send_message(chat_id='1692929855',text="Session Ended", reply_markup=get_start_button()) 

bot.infinity_polling()