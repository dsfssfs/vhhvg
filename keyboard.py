import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

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
        item1 = InlineKeyboardButton("📕математика", callback_data='math')
        item2 = InlineKeyboardButton("📗русский", callback_data='russian')
        item3 = InlineKeyboardButton("📘английский", callback_data='engl')
        item4 = InlineKeyboardButton("‍📙инф(профиль)", callback_data='inf_prof')
        item5 = InlineKeyboardButton("📕инф(обыч)", callback_data='inf')
        item6 = InlineKeyboardButton("📗биология", callback_data='biologic')
        item7 = InlineKeyboardButton("📘география", callback_data='geography')
        item8 = InlineKeyboardButton("📙общество", callback_data='social_sub')
        item9 = InlineKeyboardButton("📕обж", callback_data='safe_sub')
        item10 = InlineKeyboardButton("📗физика", callback_data='physician')
        item11= InlineKeyboardButton("📙литература", callback_data='literature')
        item12 = InlineKeyboardButton("📘история", callback_data='history')
        item13 = InlineKeyboardButton("📕химия", callback_data='chemistry')
        item14 = InlineKeyboardButton('❌закрыть❌', callback_data='back')
        sp_sub.add(item1,item2, item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13, item14)
        return sp_sub

def setup_data():
    data = InlineKeyboardMarkup()
    data.row_width = 1
    data1 = InlineKeyboardButton('добавить дату', callback_data='new_data')
    data.add(data1)
    return data
def setup_dz():
    new_dz = InlineKeyboardMarkup()
    new_dz.row_width = 1
    dz_n = InlineKeyboardButton('добавить дату', callback_data='new_data')
    new_dz.add(dz_n)
    return new_dz
