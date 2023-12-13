import telebot
API_KEY = "6956818772:AAHH5H0ejgWF3zkRY6eydgPo8geKdQj8yek"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])  #/start
def start(message):
    bot.reply_to(message,"Hello I am Dr. Aung Win Htut")

@bot.message_handler(commands=['help'])  #/start
def help(message):
    bot.reply_to(message,"What can i do for you?")


bot.polling()


