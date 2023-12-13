#Preparing Python Program for bot usage
import telebot
from telebot import types
API_Key = "6399052487:AAGNP-38DgSc_Y_P8m36PZ4oZPV-4vy5afM"

bot = telebot.TeleBot(API_Key)

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to (message, "Hello! I am KTHHMaths Bot to help you with your maths! Type 1 for 1 digit, 2 for 2 digits, 3 for 3 digits to play with the numbers!")

@bot.message_handler(func=lambda message: True)
def process_integer_input(message):
  # Extract the user input from the message
  user_input = message.text
  # Check if the received message is a valid integer
  if user_input.isdigit():
    # Convert the string to an integer
    user_input_int = int(user_input)
    if user_input_int not in (1, 2, 3):
      bot.reply_to(message, 'Invalid input! Please enter 1, 2 or 3 only.')
    elif ValueError:
      bot.reply_to(message,f'Your have selected {user_input_int} digit values to play!')
    if not user_input.isdigit():
      bot.reply_to(message, 'You have keyed in non-digit values! Please enter 1, 2 or 3 only!')
  else:
    bot.reply_to(message, f'You have input invalid number! Please enter 1, 2 or 3 only!')

# Defining 1 digit/ 2 digit/ 3 digit ranges to play
  if user_input_int == 1:
    n1 = 9
    bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
    bot.reply_to(message, "How many numbers to add/ substract?")
  elif user_input_int == 2:
    n1 = 99
    bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
    bot.reply_to(message, "How many numbers to add/ substract?")
  elif user_input_int == 3 :
    n1 = 999
    bot.reply_to(message, f'You will be adding/substracting numbers between -{n1} and {n1}!')
    bot.reply_to(message, "How many numbers to add/ substract?")
  else :
    bot.reply_to(message, "You have selected invalid input for adding/substracting numbers to play ! Please enter 1, 2 or 3 only.")

# Defining How many numbers to play?
  @bot.message_handler(func=lambda message: True)
  def process_integer_input(message):
    # Extract the user input from the message
    user_input1 = update.message.text
    # Check if the received message is a valid integer
    if user_input1.isdigit():
      # Convert the string to an integer
      user_input_int1 = int(user_input1)
    else:
     bot.reply_to(message, f'Invalid input!')

    bot.reply_to(message, "You have selected to play {user_input_int1} numbers! Let's start!")

bot.polling()