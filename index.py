import requests
from time import sleep
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
	def unpinmessage(chat):
		params = {'chat_id': chat}
		response = requests.post(url + 'unpinChatMessage', data=params)
	def sendmessage(chat, text):  
		params = {'chat_id': chat, 'text': text}
		response = requests.post(url + 'sendMessage', data=params)
		return response
	def pinmsg(chat,message):
		params = {'chat_id': chat, 'message_id': message}
		response = requests.post(url + 'pinChatMessage', data=params)
		return response
	def spinmsg(chat,message):
		params = {'chat_id': chat, 'message_id': message}
		response = requests.post(url + 'pinChatMessage' + '?disable_notification', data=params)
		return response
	def getmsgtext(update):
		text = update['message']['text']
		return text
	def getme():
		response = requests.post(url + 'getMe')
		return response
	def editmsg(chat,msgid,text):
		params = {'chat_id': chat, 'message_id': msgid,'text':text}
		response = requests.post(url + 'editMessageText', data=params)
		return response																						#last
	getupdatesjson(url)
	while True:
		lastmsg = str(getmsgtext(lastupdate(getupdatesjson(url))))
		lastmsgid = str(getmsgid(lastupdate(getupdatesjson(url))))
		print('last update message id: ' + lastmsgid)
		print('last recieved message: ' + "'" + lastmsg + "'")
		chs = input("$")
		if chs == "pin":
			chat = getchatid(lastupdate(getupdatesjson(url)))
			anons = input('!')
			pin1 = input('pin: ')
			if anons == "":
				anons = "❗Всё как обычно" 
			else:
				anons = '❗' + anons
			if pin1 == 'деф':
				pin = "⚔🖤️В деф!\n🛡🖤️В деф! \n \n " + anons
			elif pin1 == "-ф":
				pin = "⚔️🍆Ферма\n🛡🖤️В деф!\n \n " + anons
			elif pin1 == "-р":
				pin = "⚔️🌹Рассвет\n🛡🖤️В деф!\n \n " + anons
			elif pin1 == "-м":
				pin = "⚔️🦇Ночь\n🛡🖤️В деф!\n \n " + anons
			elif pin1 == "-о":
				pin = "⚔️☘️Оплот\n🛡🖤️В деф!\n \n " + anons
			elif pin1 == "-т":
				pin = "⚔️🐢Тортуга\n🛡🖤️В деф!\n \n " + anons
			elif pin1 == "-а":
				pin = "⚔️🍁Амбер\n🛡️🖤В деф!\n \n " + anons
			elif pin1 == "-фф":
				pin = "⚔️🍆Ферма\n🛡️🍆Ферма\n \n " + anons
			elif pin1 == "-рф":
				pin = "⚔️🌹Рассвет\n🛡️🌹Рассвет\n \n " + anons
			elif pin1 == "-мф":
				pin = "⚔️🦇Ночь\n🛡🦇Ночь\n \n " + anons
			elif pin1 == "-оф":
				pin = "⚔️☘️Оплот\n🛡☘️Оплот\n \n " + anons
			elif pin1 == "-тф":
				pin = "⚔️🐢Тортуга\n🛡🐢Тортуга\n \n " + anons
			elif pin1 == "-аф":
				pin = "⚔️🍁Амбер\n🛡🍁Амбер\n \n " + anons
			elif pin1 == "pp":
				pin = pin0 
			else:
				pin = pin1
			sendmessage(chat, pin)	
			msgid = getmsgid(lastupdate(getupdatesjson(url))) + 1
			pinmsg(chat, msgid)
			print("pinned " + str(getmsgid(lastupdate(getupdatesjson(url)))) + " in chat " + str(chat))
		elif chs == "spin":
			chat = getchatid(lastupdate(getupdatesjson(url)))
			pin1 = input('pin: ')
			if pin1 == 'деф':
				pin = "🛡️🖤В деф!"
			elif pin1 == "-ф":
				pin = "⚔️🍆Ферма"
			elif pin1 == "-р":
				pin = "⚔️🌹Рассвет"
			elif pin1 == "-м":
				pin = "⚔️🦇Ночь"
			elif pin1 == "-о":
				pin = "⚔️☘️Оплот"
			elif pin1 == "-т":
				pin = "⚔️🐢Тортуга"
			elif pin1 == "-а":
				pin = "⚔️🍁Амбер"
			elif pin1 == "pp":
				pin = pin0 
			else:
				pin = pin1
			sendmessage(chat, pin)
			msgid = getmsgid(lastupdate(getupdatesjson(url))) + 1
			spinmsg(chat, msgid)
			print("silently pinned " + str(getmsgid(lastupdate(getupdatesjson(url)))) + " in chat " + str(chat))
		elif chs == "ans":
			chat = getchatid(lastupdate(getupdatesjson(url)))
			text = input(">>")
			sendmessage(chat, text)
			print("sent message " + text)
		elif chs == "manual":
			chat1 = input('chat id: ')
			if chat1 == "reirose":
				chat = 352318827
			elif chat1 == "evgenon":
				chat = 616037199
			elif chat1 == "iiba":
				chat = -1001247451220
			elif chat1 == "kys":
				chat = -1001403325063
			else:
				chat = chat1
			msg = input('>>')
			sendmessage(chat, msg)
		elif chs == "prepin":
			prepin = open('8a6f503814aa4a7cd863e68c7778fbdb', 'w')
			pin = input('Prepin: ')
			prepin.write(pin)
			prepin.close()
		elif chs == "unpin":
			chat = getchatid(lastupdate(getupdatesjson(url)))
			unpinmessage(chat)
		elif chs == "pprun":
			pp = open('8a6f503814aa4a7cd863e68c7778fbdb', 'r')
			for line in pp:
				if line == 'деф':
					pin0 = "🛡️🖤В деф!"
				elif line == "-ф":
					pin0 = "⚔️🍆Ферма"
				elif line == "-р":
					pin0 = "⚔️🌹Рассвет"
				elif line == "-м":
					pin0 = "⚔️🦇Ночь"
				elif line == "-о":
					pin0 = "⚔️☘️Оплот"
				elif line == "-т":
					pin0 = "⚔️🐢Тортуга"
				elif line == "-а":
					pin0 = "⚔️🍁Амбер"
				print(">>>Added "+pin0+" to zero pin<<<")
			pp.close()
		elif chs == 'editmsg':																					#last
			chat = getchatid(lastupdate(getupdatesjson(url)))
			msgid = input('message id:')
			text = input('new text:')
			editmsg(chat,msgid,text)
		elif chs == "kill":
			exit()
		else:
			print("*shrug*")
		os.system('cls')