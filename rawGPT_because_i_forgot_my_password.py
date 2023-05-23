
import openai
# pip install openai  

openai.api_key = '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' # 'YOUR_API_KEY'
# name?: My_Test_Key_For_Python_API_Test

messages_dave = [ {"role": "system", "content": "software developer."} ]

while True:

  message = "null"

  while message is not "x" and message is not "exit":
    message = input("input : ")
    messages_dave.append({"role": "user", "content": message},)
    chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages_dave )
    reply = chat.choices[0].message.content
    print(f" \n{reply}\n")
    messages_dave.append({"role": "assistant", "content": reply})

