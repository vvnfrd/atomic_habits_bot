from django.core.management import BaseCommand
from bot.main_bot import bot


class Command(BaseCommand):

    def handle(self, *args, **options):
        bot.infinity_polling()