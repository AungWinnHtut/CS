# pip install pyTelegramBotAPI
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# API_KEY = "6478428152:AAHdcwD0x0IzvD2twcN5ORTwbFae58gjJTU" #GreenHackers
API_KEY = "6755851932:AAHE0EP6aX7As10QF7YnDmHJB9E4dor-u7k" #Python Myanmar

bot = telebot.TeleBot(API_KEY)




gd_subjs = [
    ["Python C (GD)", "C (GD)"],
    ["C++ C (GD)", "Arduino C (GD)"],
    ["C# C (GD)", "/start"]
] 

# Create a ReplyKeyboardMarkup with the provided options
gd_kb = ReplyKeyboardMarkup(resize_keyboard=True)
for row in gd_subjs:
    gd_kb.add(*[KeyboardButton(option) for option in row])


# Start Menu
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton('လက်ရှိတက်ရောက်နိုင်သော သင်တန်းများ'))
start_kb.add(KeyboardButton('စာမေးရန်'))
start_kb.add(KeyboardButton('ဆက်သွယ်စုံစမ်းရန်'))

# Class List
class_kb = ReplyKeyboardMarkup(resize_keyboard=True)
class_kb.add(KeyboardButton('Google Drive Video Lessons ဖြင့် သင်ကြားသော သင်တန်းများ'))
class_kb.add(KeyboardButton('Zoom Class သင်တန်းများ'))
class_kb.add(KeyboardButton('/start'))

# Question 
q_kb = ReplyKeyboardMarkup(resize_keyboard=True)
q_kb.add(KeyboardButton('https://www.facebook.com/AungWinHtutGH/'))
q_kb.add(KeyboardButton('/start'))

# Contact 
c_kb = ReplyKeyboardMarkup(resize_keyboard=True)
c_kb.add(KeyboardButton('Contact us at:+9595506082'))
c_kb.add(KeyboardButton('/start'))


@bot.message_handler(commands=['start'])
def start(message):    
    user = message.from_user
    bot.send_message(message.chat.id, f"မင်္ဂလာပါ {user.first_name}! Choose an option:", reply_markup=start_kb)



@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"ဘာကူညီပေးရမလဲ ခင်ဗျ။ ကျွန်တော် Dr. အောင်ဝင်းထွဋ်ပါ ခင်ဗျာ")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):    
    if 'လက်ရှိတက်ရောက်နိုင်သော သင်တန်းများ' in message.text:
        bot.send_message(message.chat.id, f"သင်တန်းများ", reply_markup=class_kb)  
    elif 'စာမေးရန်' in message.text:
        bot.send_message(message.chat.id, f"စာမေးရန်", reply_markup=q_kb)  
    elif 'ဆက်သွယ်စုံစမ်းရန်' in message.text:
        bot.send_message(message.chat.id, f"ဆက်သွယ်စုံစမ်းရန်", reply_markup=c_kb) 
    elif 'Google Drive Video Lessons ဖြင့် သင်ကြားသော သင်တန်းများ' in message.text:
        bot.send_message(message.chat.id, f"Google Drive Video Lessons ဖြင့် သင်ကြားသော သင်တန်းများ", reply_markup=gd_kb) 
    elif 'C (GD)' in message.text:
        bot.send_message(message.chat.id, f"C (GD) သင်တန်းကြေး ၁၀၀၀၀၀ ကျပ်\nသင်တန်းဖွင့်မည့်ရက် ၂-၁၂-၂၀၂၃\nသင်ကြားမည့် အချိန် စနေ၊ တနင်္ဂနွေ ညနေ ၇-၈")
    elif 'C++ (GD)' in message.text:
        bot.send_message(message.chat.id, f"C++ (GD) ")
    elif 'C# (GD)' in message.text:
        bot.send_message(message.chat.id, f"C# (GD)")
    elif 'Arduino (GD)' in message.text:
        bot.send_message(message.chat.id, f"Arduino (GD)")
    elif 'Python (GD)' in message.text:
        bot.send_message(message.chat.id, f"Python (GD)")
    
bot.polling()
