from django.conf import settings
import requests
import telebot
from users.models import User


bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if User.objects.filter(telegram_id=message.from_user.id).exists():
        text = ('Здарова, ты авторизирован\n'
                'Бот будет присылать уведомления о привычках\n'
                'Авторизация и регистрация осуществляется следующими коммандами:\n'
                '/auth [email] [password]\n/register [email] [password]\n'
                'Также доступны следующие комманды:\n/exit - Выход с акка')
    else:
        text = ('Здарова, ты не авторизирован\n'
                'Бот будет присылать уведомления о привычках\n'
                'Авторизация и регистрация осуществляется следующими коммандами:\n'
                '/auth [email] [password]\n/register [email] [password]\n'
                'Также доступны следующие комманды:\n/exit - Выход с акка')

    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text.lower().split(' ')[0] == '/auth')
def auth(message):
    if User.objects.filter(telegram_id=message.from_user.id).exists():
        text = 'Ты уже авторизирован'
    else:
        user_email = message.text.lower().split(' ')[1]
        user_pass = message.text.lower().split(' ')[2]

        data = {"email": user_email, "password": user_pass}

        response = requests.post('http://127.0.0.1:8000/users/token/', data=data)

        if "access" in response.json():
            user = User.objects.get(email=user_email)
            user.telegram_id = message.from_user.id
            user.save()
            text = 'Ты успешно авторизировался!'
        else:
            text = 'Неверный логин или пароль!'

    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text.lower().split(' ')[0] == '/register')
def register(message):
    if User.objects.filter(telegram_id=message.from_user.id).exists():
        text = 'Ты уже зарегестрирован!'
    else:
        user_email = message.text.lower().split(' ')[1]
        user_pass = message.text.lower().split(' ')[2]
        data = {
            "email": user_email,
            "password": user_pass
        }

        response = requests.post('http://127.0.0.1:8000/users/register/', data=data)

        if "password" in response.json():
            user = User.objects.get(email=user_email)
            user.telegram_id = message.from_user.id
            user.save()
            text = 'Ты успешно зареган!'
        else:
            text = 'Пользователь с такой почтой уже существует!'

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['exit'])
def exit(message):

    if not User.objects.filter(telegram_id=message.from_user.id).exists():
        text = 'Так не авторизирован'
    else:
        user = User.objects.get(telegram_id=message.from_user.id)
        user.telegram_id = None
        user.save()
        text = 'Ты успешно вышел из аккаунта'

    bot.send_message(message.chat.id, text)
