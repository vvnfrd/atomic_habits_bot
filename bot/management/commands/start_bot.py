import asyncio

from django.conf import settings
from django.core.management import BaseCommand
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(settings.BOT_TOKEN)

class Command(BaseCommand):
    @bot.message_handler(commands=['help', 'start'])
    async def send_welcome(message):
        text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
        await bot.reply_to(message, text)


    # @bot.message_handler(func=lambda message: True)
    # async def echo_message(message):
    #     await bot.reply_to(message, message)


    @bot.message_handler(commands=['authorization'])
    async def send_welcome(message):
        text = 'Введите свою почту:'
        await bot.reply_to(message, text)

    def handle(self, *args, **kwargs):
        asyncio.run(bot.polling())

