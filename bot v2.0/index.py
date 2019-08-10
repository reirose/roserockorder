from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import re, time, math, random, uuid
from telegram.ext.messagehandler import MessageHandler


#vars and else

chats = [-1001222465858, -1001247451220]
unixtime = {
    'm': 60,
    'h': 3600,
    'd': 86400,
    'w': 604800
}
debug = 1


#commands


def start(bot,update):
    bot.sendMessage(chat_id = update.message.chat_id, text='Привет.')
def status(bot, update):
    text1 = 'Статус: Работает\n' + time.asctime()
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id, text=text1)
    print('Кто-то проверил, работаю ли я.\nНадеюсь, это ты.')
    print(str(update.message.user))
def kill(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = 'eeeeh.')
    print('Меня убили.')
    exit()
def bothelp(bot, update):
    print('тут должен быть список команд, но я сам ещё нихуя не понимаю ')
    bot.sendMessage(chat_id = update.message.chat_id, text = 'я ещё сам нихуя не знаю\nотъебитесь')
def nowtime(bot, update):
    hourmin = time.strftime('%H:%M')
    texttime = 'Сейчас ' + hourmin
    bot.sendMessage(chat_id = update.message.chat_id, text = texttime)
    print('Кто-то захотел узнать время. Это ты?')
def mute(bot, update):
    if update.message.from_user.id == 352318827 or update.message.from_user.id == 698507628:
        timer = math.floor(time.time() + int(update.message.text[6:-1]) * unixtime[update.message.text[-1]])
        print(timer)
        chat_id = update.message.chat_id
        print(chat_id)
        user_id = update.message.reply_to_message.from_user.id
        print(user_id)
        bot.restrictChatMember(chat_id=chat_id, user_id=user_id, until_date = timer)
        print('Замьютили кого-то на '+str(update.message.text[6:]))
    else:
        bot.sendMessage(chat_id = update.message.chat_id, text = 'Извини, но ты не Рей.')
def randomnum(bot, update):
    lim = update.message.text[8:]
    print(lim)
    num = math.floor(random.random() * (int(lim) + 1))
    print(num)
    thrown_by = update.message.from_user.first_name
    print(thrown_by)
    bot.sendMessage(chat_id = update.message.chat_id, text = 'У *'+thrown_by+'* выпало число *'+str(num)+'*', parse_mode = 'Markdown') 
    print('У '+thrown_by+' выпало число '+str(num))


                            #main()


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    #dp.add_handler(CommandHandler('',))
    dp.add_handler(CommandHandler('random',randomnum))
    dp.add_handler(CommandHandler('help',bothelp))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('status',status))
    dp.add_handler(CommandHandler('kill',kill))
    dp.add_handler(CommandHandler('time',nowtime))
    dp.add_handler(CommandHandler('mute',mute))
    print('ktktktktktktkt')
    updater.start_polling()
    print('vrrrrrrrrrr')
    updater.idle()
    if debug == 1:
        bot.sendMessage(chat_id = update.message.chat_id, text = 'Я пробужжжжжжжжждаюсь')

if __name__ == '__main__':
    main()
