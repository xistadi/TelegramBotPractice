import requests
import config

API_link = config.API_link

updates = requests.get(API_link + 'getUpdates?offset=-1').json()

print(updates)

message = updates['result'][0]['message']

chat_id = message['from']['id']
text = message['text']

print(chat_id)
print(text)

sent_message = requests.get(API_link + f'sendMessage?chat_id={chat_id}&text=Ты написал {text}')
