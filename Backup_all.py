# from corneddonuts import Donuts
# # import pyTelegramBotAPI
# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('5784890908:AAEiDjRjFCHVmGz-q7sKbLtR-0IbgbeKaPg')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton('Начать смену✅')
#     markup.add(btn1)
#
#     bot.send_message(message.chat.id, text='Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if (message.text == 'Начать смену✅' or 'Остатки пончиков🍩'):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton(text='Остатки пончиков🍩')
#         btn2 = types.KeyboardButton(text='Закрыть смену❌')
#         btn3 = types.KeyboardButton(text='Пополнить пончики➕')
#         markup.add(btn1)
#         markup.add(btn2)
#         markup.add(btn3)
#     if (message.text == 'Начать смену✅'):
#         bot.send_message(message.chat.id, text='Смена началась')
#         new_smena = Donuts()
#         donutscorner = new_smena.StartNew()
#         donuts = new_smena.Info(donutscorner)
#         bot.send_message(message.chat.id, donuts, reply_markup=markup)
#     elif (message.text == 'Остатки пончиков🍩'):
#         new_smena = Donuts()
#         donutscorner = new_smena.StartNew()
#         donuts = new_smena.Info(donutscorner)
#         bot.send_message(message.chat.id, donuts, reply_markup=markup)
#
#     elif(message.text == 'Пополнить пончики➕'):
#         markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton(text='Розовые')
#         btn2 = types.KeyboardButton(text='Карамельные')
#         btn3 = types.KeyboardButton(text='Ванильные')
#         btn4 = types.KeyboardButton(text='Шоколадные')
#         btn5 = types.KeyboardButton(text='Вернуться в главное меню')
#         markup2.add(btn1, btn2, btn3, btn4, btn5)
#         bot.send_message(message.chat.id, text='Какие пончики приехали?', reply_markup=markup2)
#
#     if(message.text == 'Вернуться в главное меню'):
#         bot.send_message(message.chat.id, text='Возвращаю в главное меню', reply_markup=markup)
#
#     elif (message.text == 'Закрыть смену❌'):
#         markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton(text='Точно закрываю смену')
#         btn2 = types.KeyboardButton(text='Я передумал')
#         markup2.add(btn1)
#         markup2.add(btn2)
#         bot.send_message(message.chat.id, text='Вы уверены, что хотите закрыть смену?', reply_markup=markup2)
#     elif (message.text == 'Я передумал'):
#         bot.send_message(message.chat.id, text='Возвращаю в главное меню', reply_markup=markup)
#     elif (message.text == 'Точно закрываю смену'):
#         pass
#
#     @bot.message_handler(content_types=['text'])
#     def DonutsUpdater(message):
#         if (message.text == 'Розовые'):
#             bot.send_message(message.chat.id, message.text)
#
#
# bot.polling(none_stop=True)
