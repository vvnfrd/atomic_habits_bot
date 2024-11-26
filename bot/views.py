# import telebot
# from django.conf import settings
# from django.http import HttpResponse
#
# bot = telebot.TeleBot(settings.BOT_TOKEN)
#
#
# def index(request):
#     if request.method == "POST":
#         update = telebot.types.Update.de_json(request.body.decode('utf-8'))
#         bot.process_new_updates([update])
#
#     return HttpResponse('<h1>Ты подключился!</h1>')
#
# @bot.message_handler(commands=['start'])
# def start(message: telebot.types.Message):
#     name = ''
#     if message.from_user.last_name is None:
#         name = f'{message.from_user.first_name}'
#     else:
#         name = f'{message.from_user.first_name} {message.from_user.last_name}'
#     bot.send_message(message.chat.id, f'Привет! {name}\n'
#                                       f'Я бот, который будет спамить вам беседу :)\n\n'
#                                       f'Чтобы узнать больше команд, напишите /help')
