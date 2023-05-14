
import openai
import pyttsx3
# pip install pyttsx3
# pip install openai  

converter = pyttsx3.init()
converter.setProperty('rate', 160)
converter.setProperty('volume', 0.8)
voice_id_dave = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
voice_id_zira = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

openai.api_key = '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' # 'YOUR_API_KEY'
# name?: My_Test_Key_For_Python_API_Test

messages_dave = [ {"role": "system", "content": "You are an academic."} ]
messages_zira = [ {"role": "system", "content": "You are an academic."} ]
counter = 0
reply_length = 40 
  # there is a 3 request per minute restriction on chatgpt
  # setting this below 40 with a speech rate > 160 will trigger it.
reply_count = 3
  # rounds - so this number *2 total speachs

while True:

  topic = input("Debate Topic : ")
  if topic == 'x' or topic == 'exit':
    exit()
  #reply = ''
  message = 'you believe that '+topic+' is a positive, your opponant is ready and you are starting the debate, '+str(reply_length)+' words or less'

  while counter < reply_count:
    counter += 1

    if counter != 1:
      message = 'you believe that '+topic+' is a positive, your debate opponant has just said this to you: '+reply+' it is now your turn to speak, please respond in '+str(reply_length)+' words or less'
    if counter == reply_count:
      message = message+' this is your closing statement'
    messages_dave.append({"role": "user", "content": message},)
    chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages_dave )
    reply = chat.choices[0].message.content
    print(f"Dave-GPT {counter} of {reply_count}: \n{reply}\n")
    messages_dave.append({"role": "assistant", "content": reply})
    converter.setProperty('voice', voice_id_dave)
    converter.say(reply)

    message = 'you believe that '+topic+' is a negative, your debate opponant has just said this to you: '+reply+' it is now your turn to speak, please respond in '+str(reply_length)+' words or less'
    if counter == reply_count:
      message = message+' this is your closing statement'
    messages_zira.append({"role": "user", "content": message},)
    chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=messages_zira )
    reply = chat.choices[0].message.content
    print(f"Zira-GPT {counter} of {reply_count}: \n{reply}\n")
    messages_zira.append({"role": "assistant", "content": reply})
    converter.setProperty('voice', voice_id_zira)
    converter.say(reply)

    converter.runAndWait()
