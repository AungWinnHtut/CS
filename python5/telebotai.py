# pip install pyTelegramBotAPI
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# API_KEY = "6478428152:AAHdcwD0x0IzvD2twcN5ORTwbFae58gjJTU" #GreenHackers
API_KEY = "6682461367:AAFP3mfTiO1XkS6JRfRMFIB37FVFCxeviwQ"

bot = telebot.TeleBot(API_KEY)

options = [
    ["Python", "C"],
    ["C++", "Arduino"]
] 

# Create a ReplyKeyboardMarkup with the provided options
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for row in options:
    keyboard.add(*[KeyboardButton(option) for option in row])

@bot.message_handler(commands=['start'])
def start(message):    
    user = message.from_user
    bot.send_message(message.chat.id, f"မင်္ဂလာပါ {user.first_name}! Choose an option:", reply_markup=keyboard)



@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"ဘာကူညီပေးရမလဲ ခင်ဗျ။ ကျွန်တော် Dr. အောင်ဝင်းထွဋ်ပါ ခင်ဗျာ")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):    
    if 'tutorial' in message.text:
        bot.reply_to(message,'tutorial သင်ခန်းစာများကို မကြာမီ တင်ပေးသွားပါမည်')        
    elif 'online class' in message.text:
        bot.reply_to(message,'အွန်လိုင်း သင်တန်း တက်လိုပါက095506082 ကို ဆက်သွယ်ပေးပါ')
    elif 'Python' in message.text:
        bot.reply_to(message,'Python သင်တန်းကြေးက တစ်လ တစ်သိန်း ဖြစ်ပါတယ်။ အွန်လိုင်း သင်တန်း တက်လိုပါက095506082 ကို ဆက်သွယ်ပေးပါ')
    elif 'C++' == message.text:
        bot.reply_to(message,'C++ သင်တန်းကြေးက တစ်လ တစ်သိန်း ဖြစ်ပါတယ်။ အွန်လိုင်း သင်တန်း တက်လိုပါက095506082 ကို ဆက်သွယ်ပေးပါ')
    elif 'C' == message.text:
        bot.reply_to(message,'C သင်တန်းကြေးက တစ်လ တစ်သိန်း ဖြစ်ပါတယ်။ အွန်လိုင်း သင်တန်း တက်လိုပါက095506082 ကို ဆက်သွယ်ပေးပါ')
    elif 'Arduino' in message.text:
        bot.reply_to(message,'Arduino သင်တန်းကြေးက တစ်လ တစ်သိန်း ဖြစ်ပါတယ်။ အွန်လိုင်း သင်တန်း တက်လိုပါက095506082 ကို ဆက်သွယ်ပေးပါ')


bot.polling()
