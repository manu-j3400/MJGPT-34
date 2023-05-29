import openai
import os

x = 0

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.environ['MJGPT']

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
      {
        "role": "user",
        "content": prompt
      }
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

while x == 0:
  prompt = input("Ask a question: ")
  print(get_completion(prompt))
