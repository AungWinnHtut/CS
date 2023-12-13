from googletrans import Translator
import os

input_text_file = open('burmese.txt','r',encoding='utf-8')
input_text = input_text_file.readlines()
input_text_file.close()

translator = Translator()
os.system('del translate.txt')
file = open('translate.txt','a',encoding='utf-8')

for line in input_text:
    ans = translator.translate(line, dest='en')
    print(ans.text)
    file.write(ans.text)

file.close()
os.system('notepad translate.txt')
