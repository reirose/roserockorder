import requests
import time
import os

url = "https://api.telegram.org/bot674745415:AAFQZvzno4kljKq0ITDyViW8RhWsHQWRTXA/"
class BotHandler:
	chats = [1001247451220, -1001428724930]
	def getupdatesjson(request):  
		response = requests.get(request + 'getUpdates')
		return response.json()
	def lastupdate(data):  
		results = data['result']
		total_updates = len(results) - 1
		return results[total_updates]
	def getchatid(update):  
		chat_id = update['message']['chat']['id']
		return chat_id
	def getmsgid(update):  
		msg_id = update['message']['message_id']
		return msg_id
	def sendmessage(chat, text):  
		params = {'chat_id': chat, 'text': text}
		response = requests.post(url + 'sendMessage', data=params)
		return response
	def editmsg(chat,msgid,text):
		params = {'chat_id': chat, 'message_id': msgid,'text':text}
		response = requests.post(url + 'editMessageText', data=params)
		return response		
	os.system('title timer()')
	msgid = getmsgid(lastupdate(getupdatesjson(url))) + 1
	while True:
		time.asctime()
		msg = time.strftime('%d %b %Y\n%X (MSK-2)')
		editmsg(352318827, msgid, msg)
		os.system('cls')
		print(msg)
		time.sleep(1)