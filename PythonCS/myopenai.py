import os
# pip install openai=0.28.0
import openai

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


# Example usage
result = query_gpt3("write a python program which can calculate BMI")
print(result)
with open('aipython.py','w') as file:
    file.write(result)

os.system('python aipython.py')