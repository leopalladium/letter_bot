import telebot
from telebot import types
import config
import texts
import pics
bot = telebot.TeleBot(config.token)



@bot.message_handler(commands=['start'])
def welcome(message): 
        
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да")
    item2 = types.KeyboardButton("Нет")
 
    markup.add(item1, item2)

    bot.send_message(message.chat.id, texts.m1, parse_mode='Markdown', 
                     reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def response_1(message):

    
     markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
     item11 = types.KeyboardButton("Перевернуть конверт")
     markup1.add(item11)
    
     markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
     item21=types.KeyboardButton("Открыть")
     markup2.add(item21)

     markup3=types.ReplyKeyboardMarkup(resize_keyboard=True)
     item31=types.KeyboardButton("Да!") #дописать текст
     markup3.add(item31)

     #if conditions for replies

     if message.chat.type == 'private':
        if message.text == 'Да':
            bot.send_message(message.chat.id, texts.m21, parse_mode='Markdown', reply_markup=markup1)
            bot.send_message(message.chat.id, texts.m22, parse_mode="Markdown",)
            env1 = open('картино4ки\Без имени-1.png', 'rb')
            bot.send_sticker(message.chat.id, env1)
            bot.send_message(message.chat.id, "подсказка: переверни конверт")
        elif message.text == 'Нет':
            bot.send_message(message.chat.id, "*Почтальон*: Хорошо, до свидания!" , parse_mode="Markdown")
            bot.send_message(message.chat.id, "_Почтальон уходит дальше работать, а твой день продолжается как обычно. Спасибо за игру!_", parse_mode="Markdown" )
            bot.send_message(message.chat.id, "подсказка: перезапустить бота - /start", reply_markup=types.ReplyKeyboardRemove())
        env2=open('картино4ки\конверт-2.png', 'rb')
        if message.text == 'Перевернуть конверт':
            bot.send_message(message.chat.id, "_перед тобой конверт с сердечком на задней стороне_" , parse_mode="Markdown")
            bot.send_sticker(message.chat.id, env2, reply_markup=markup2)
        if message.text == 'Открыть':
            bot.send_message(message.chat.id, "_ты аккуратно открываешь конверт_" , parse_mode="Markdown")
            #bot.send_message(message.chat.id, "_внутри лежит небольшое письмо_" , parse_mode="Markdown") 
            env3=open('картино4ки\конверт 3.png', 'rb')
            bot.send_sticker(message.chat.id, env3, reply_markup=markup3)
        if message.text == 'Да!':
            bot.send_message(message.chat.id, texts.m3, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
            t1=open('t1.png', 'rb')
            t2=open('t2.png', 'rb')
            t3=open('t3.png', 'rb')
            t4=open('t4.png', 'rb')
            t5=open('t5.png', 'rb')
            t6=open('t6.png', 'rb')
            t7=open('t7.png', 'rb')
            t8=open('t8.png', 'rb')
            t9=open('t9.png', 'rb')
            t10=open('t10.png', 'rb')
            t11=open('t11.png', 'rb')
            t12=open('t12.png', 'rb')
            t13=open('t13.png', 'rb')
            t14=open('t14.png', 'rb')
            bot.send_sticker(message.chat.id, t1)
            bot.send_sticker(message.chat.id, t2)
            bot.send_sticker(message.chat.id, t3)
            bot.send_sticker(message.chat.id, t4)
            bot.send_sticker(message.chat.id, t5)
            bot.send_sticker(message.chat.id, t6)
            bot.send_sticker(message.chat.id, t7)
            bot.send_sticker(message.chat.id, t8)
            bot.send_sticker(message.chat.id, t9)
            bot.send_sticker(message.chat.id, t10)
            bot.send_sticker(message.chat.id, t11)
            bot.send_sticker(message.chat.id, t12)
            bot.send_sticker(message.chat.id, t13)
            bot.send_sticker(message.chat.id, t14)    
bot.polling(none_stop=True)