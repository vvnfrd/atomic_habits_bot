from rest_framework.test import APITestCase
from users.models import User
from users.management.commands.csu import Command


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        Command.handle(self)

    def test_csu(self):
        admin = User.objects.get(email='admin@gmail.com')

        """Тестирование функции создания привычки"""

        # print(User.objects.get(email='admin@gmail.com').email, admin.email)
        self.assertEqual(User.objects.get(email='admin@gmail.com').email, admin.email)
        self.assertEqual(User.objects.get(email='admin@gmail.com').password, admin.password)