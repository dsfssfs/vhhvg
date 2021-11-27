
import telebot
from bd import *
from keyboard import *


token = '2017410421:AAFmIJPHvet56Cs356kn7HN_ECH4NbFKkmQ'
bot = telebot.TeleBot(token)
admin = 1933108157



@bot.message_handler(commands=['start'])
def start(message):

    if message.chat.id == admin:
        bot.send_message(message.chat.id, text='hi admin', reply_markup=admin_menu())
    else:
        bot.send_message(message.chat.id, text='hi user', reply_markup=user_menu())

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '📚Д/З📚':
        bot.send_message(message.from_user.id, "Выбери предмет:", reply_markup=spisok_dz())

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '🩸добавить дз🩸':
        bot
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    def edit(message):
        if call.data == 'back':
            bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id,  reply_markup=None)
            bot.send_message(chat_id=call.from_user.id, text = "✅успешно закрыто")
        if call.data == "math":
            bot.send_message(call.from_user.id, text= "выберите дату", reply_markup=data())
        if call.data == "russian":
            bot.send_message(call.from_user.id, text= "выберите дату", reply_markup=data())



bot.polling()