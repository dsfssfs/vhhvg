import os
from unittest.mock import call

import telebot

import keyboa

import sqlite3

from keyboa import Keyboa
from keyboa.keyboards import keyboa_maker
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

token = '2017410421:AAFmIJPHvet56Cs356kn7HN_ECH4NbFKkmQ'
bot = telebot.TeleBot(token)
admin = 1933108157
connect = sqlite3.connect('all.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS subjects(
math text,
russian text,
chemistry text,
obg text,
obshestvo text,
geography text)

    """)
connect.commit()


def user_menu():
    main = telebot.types.ReplyKeyboardMarkup(True)

    main.row('📚Д/З📚', '⏳Расписание звонков⏳' )
    main.row('👨‍🏫Список учителей👨‍🏫', '📡Изменения📡')
    return main

def admin_menu():
    main = telebot.types.ReplyKeyboardMarkup(True)
    main.row('📚Д/З📚', '⏳Расписание звонков⏳' )
    main.row('👨‍🏫Список учителей👨‍🏫', '📡Изменения📡')
    main.add('🩸добавить дз🩸')

    return main
def spisok_dz():

        sp_sub = InlineKeyboardMarkup()
        sp_sub.row_width = 4
        item1 = InlineKeyboardButton("математика", callback_data='math')
        item2 = InlineKeyboardButton("русский", callback_data='russian')
        item3 = InlineKeyboardButton("английский", callback_data='engl')
        item4 = InlineKeyboardButton("информатика(профиль)", callback_data='inf_prof')
        item5 = InlineKeyboardButton("информаткиа(обыч)", callback_data='inf')
        item6 = InlineKeyboardButton("биология", callback_data='biologic')
        item7 = InlineKeyboardButton("география", callback_data='geography')
        item8 = InlineKeyboardButton("общество", callback_data='social_sub')
        item9 = InlineKeyboardButton("обж", callback_data='safe_sub')
        item10 = InlineKeyboardButton("физика", callback_data='physician')
        item11= InlineKeyboardButton("литература", callback_data='literature')
        item12 = InlineKeyboardButton("история", callback_data='history')
        item13 = InlineKeyboardButton("химия", callback_data='chemistry')
        item14 = InlineKeyboardButton('❌закрыть❌', callback_data='back')
        sp_sub.add(item1,item2, item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13, item14)
        return sp_sub

def data():
    data = InlineKeyboardMarkup()
    data.row_width = 1
    data1 = InlineKeyboardButton('20.11.2021', callback_data='20.11.2021')
    data2 = InlineKeyboardButton('21.11.2021', callback_data='21.11.2021')
    item1 = InlineKeyboardButton('❌закрыть❌', callback_data='back')
    data.add(data1, data2, item1)
    return data

@bot.message_handler(commands=['start'])
def start(message):

    if message.chat.id == admin:
        bot.send_message(message.chat.id, text='hi admin', reply_markup=admin_menu())
    else:
        bot.send_message(message.chat.id, text='hi user', reply_markup=user_menu())
def del_klav():

    del1 = telebot.types.ReplyKeyboardRemove()
    return del1

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '📚Д/З📚':
        bot.send_message(message.from_user.id, "Выбери предмет:", reply_markup=spisok_dz())
    if call.data == 'back':
        bot.send_message(call.message.chat.id, text = 'закрыто', reply_markup = del_klav())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "math":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id = call.message.message_id, text = 'выбери дату', reply_markup = data())
    if call.data == "russian":
        bot.send_message(call.from_user.id, text= "выберите дату", reply_markup=data())


bot.polling()