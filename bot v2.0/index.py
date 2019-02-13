from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import re
import time
from telegram.ext.messagehandler import MessageHandler

chats = [-1001222465858, -1001247451220]

def start(bot,update):
    bot.sendMessage(chat_id = update.message.chat_id, text='Привет.')
def status(bot, update):
    text1 = 'Статус: Работает\n' + time.asctime()
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id, text=text1)
    print('Кто-то проверил, работаю ли я.\nНадеюсь, это ты.')
    print(str(update.message.user_id))
def kill(bot, update):
    print('Меня убили.')
    exit()
def help(bot,update):
    print('Хелп')
    bot
def time(bot,update):
    timee = time.asctime()
    bot.sendmessage(chat_id = update.message.chat_id, text = timee)
    print('Кто-то захотел узнать время. Это ты?')
                            #main()
def main():
    updater = Updater('674745415:AAFQZvzno4kljKq0ITDyViW8RhWsHQWRTXA')
    dp = updater.dispatcher
    #dp.add_handler(CommandHandler('',))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('status',status))
    dp.add_handler(CommandHandler('kill',kill))
    dp.add_handler(CommandHandler('time',time))
    print('ktktktktktktkt')
    updater.start_polling()
    print('vrrrrrrrrrr')
    updater.idle()

if __name__ == '__main__':
    main()