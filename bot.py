# Настроить бота на отправку сообщений +
# Сделать чтобы он рандомно отправлял числа в "руку" игрока +
# Сделать чтобы брал "карты" себе +-
# Научить считать сумму +
# Сделать чтобы сравнивал с "рукой" игрока +
# В будущем может прикрутить визуал и возможность добирать(и игроку и боту), сплитить и добавить банк; добавить кнопку
# Вебхуки / гетайпдейтс
#                                                                                                                                                                                                                                                                                                                                                                                                                 Если залью это на гх и найду где-то в будущем, то хочу напомнить себе, что Саша лучшая <3 ❤💙💜🖤💞 вау ебать вс код воспринимает юникодовские эмодзи 🚽 
import telebot
from telebot import types
import random
import time
import requests
token = '1371006028:AAFn3c6F0DoutVUzdbRhjScdKQPuxXNbC-Y'
#MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates?offset=10'.format(token=token)
#https://api.telegram.org/bot1371006028:AAFn3c6F0DoutVUzdbRhjScdKQPuxXNbC-Y/getUpdates?offset=10
bot = telebot.TeleBot(token)
markup = types.InlineKeyboardMarkup()
kartinki = ["Валет", "Дама", "Король", "Туз"]
summa = 0
summabot = 0
summ = []

    
""" @bot.message_handler(content_types='text')
def start(message):
    #getupdates(message)
    btn1 = types.InlineKeyboardButton(text= "Играть", callback_data='yes')
    markup.add(btn1)
    msg0 = bot.send_message(message.from_user.id, 'Wanna play?', reply_markup=markup)
    @bot.callback_query_handler(func=lambda call: True)
    def check(message):
        if btn1.callback_data == 'yes':
            blackjack(message) 
            time.sleep(0.5)
            bot.delete_message(message.from_user.id, msg0.message_id)
        else:
            bot.send_message(message.from_user.id, "Ну бб тогда")
def blackjack(message):
    #getupdates(message)
    card = [random.randint(3, 14),random.randint(3, 14),random.randint(3, 14),random.randint(3, 14)]
    summ = card.copy() 
    msg = bot.send_message(message.from_user.id, str(card))
    for x in range(len(card)):
        for t in range(11,15):
            if card[x] == t and t == 11:
                card[x] = kartinki[0]
            elif card[x] == t and t == 12:
                card[x] = kartinki[1]
            elif card[x] == t and t == 13:
                card[x] = kartinki[2]
            elif card[x] == t and t == 14:
                card[x] = kartinki[3]               
    #card.append(random.randint(11, 14))
    for x in range(len(summ)):
        for t in range(11,15):
            if summ[x] == t and t !=14:
                summ[x] = 10
            elif summ[x] == t and t == 14:
                summ[x] = 11
    summa = summ[0] + summ[1]
    summabot = summ[2] + summ[3]
    if summa == 21 and summabot != 21:
        bot.send_message(message.from_user.id, "Ваши карты: "+str(card[0])+', '+str(card[1]))
        bot.send_message(message.from_user.id, 'У Вас блекджек, Вы победили!')
    elif summa == 21 and summabot == 21:
        bot.send_message(message.from_user.id, "Ничья!")
    else:
        bot.send_message(message.from_user.id, "Ваши карты: "+str(card[0])+', '+str(card[1]) + '\n'+ "Ваш счёт: " + str(summa))
        time.sleep(0.5)
        bot.send_message(message.from_user.id, "Карты крупье: "+ str(card[2])+", "+'*****'+'\n'+"Счёт крупье: "+str(summabot))
        time.sleep(0.5)
        if summa > summabot:
            bot.send_animation(message.from_user.id, 'https://tenor.com/view/aot-attack-on-titan-gif-21478955')
            msg2 = bot.send_message(message.from_user.id, "Вы выиграли!", reply_markup=markup)
            #bot.send_photo(message.from_user.id, 'https://sun9-80.userapi.com/impg/taRHXKr_qUSeGfzCsYeGx6qFj_1yV7bjBG1vpA/j24ntxDjM7g.jpg?size=1080x1080&quality=95&sign=9e4188b54c00ae80411ef33b023be4f9&type=album')
        elif summa == summabot:
            msg2 = bot.send_message(message.from_user.id, "Ничья!", reply_markup=markup)
        elif summa < summabot:
            msg2 = bot.send_message(message.from_user.id, "Вы проиграли!", reply_markup=markup)
    bot.delete_message(message.from_user.id, msg.message_id)
    time.sleep(5)
    bot.edit_message_reply_markup(message.from_user.id, msg2.message_id) """
""" def getupdates(message, offset = 0):
    response = requests.get('https://api.telegram.org/bot{token}/getUpdates')
    result = response.json()
    print(result) """
bot.infinity_polling() 