
import openai
# pip install openai  

openai.api_key = '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' # 'YOUR_API_KEY'
openai.api_key = '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'
openai.api_key = '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'
# name?: My_Test_Key_For_Python_API_Test

messages_dave = [ {"role": "system", "content": "helpfull assistant"} ]

while True:

  message = "null"

  while message != "x" and message != "exit":
    message = input("input : ")
    messages_dave.append({"role": "user", "content": message},)
    chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages_dave )
    reply = chat.choices[0].message.content
    print(f" \n{reply}\n")
    messages_dave.append({"role": "assistant", "content": reply})

# come up with an original name for a weapon in an rpg game, in precisly this format: "Name - Some flavour text, no more than 15 words" this one is a sword that boosts intelligence.