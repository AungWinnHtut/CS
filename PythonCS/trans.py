import os
# pip install openai
import openai
# from googletrans import Translator, LANGUAGES
# openai API key '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'
def translate_text(text,fname, dest_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)    
    print(f"Translated Text: {translation.text}")
    with open(fname,'w',encoding='utf-8') as out_file:
        out_file.write(translation.text)

def query_gpt3(prompt, model="text-davinci-003", max_tokens=100):
    openai.api_key = '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'  # Replace with your actual API key

    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"




# Start Here Example usage
if not os.path.exists('english.txt'):
    print('no such file')
    exit(1)
with open('english.txt','r',encoding='utf-8') as input_file:
    english_txt = input_file.read()

output_filename = 'burmese.txt'
translate_text(english_txt, output_filename )  # Translates 'Hola mundo' from Spanish to English






# Example usage
result = query_gpt3("Translate 'Hello, world!' to Spanish")
print(result)
