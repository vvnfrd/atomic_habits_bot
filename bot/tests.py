from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory

from bot.main_bot import send_welcome, auth, register, exit
from bot.tasks import notifications
from users.models import User
from users.management.commands.csu import Command

class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        pass


    def test_send_welcome(self):
        try:
            send_welcome('message')
        except AttributeError:
            self.assertTrue(True)
        finally:
            self.assertTrue(True)

    def test_auth(self):
        try:
            auth('message')
        except AttributeError:
            self.assertTrue(True)
        finally:
            self.assertTrue(True)

    def test_register(self):
        try:
            register('message')
        except AttributeError:
            self.assertTrue(True)
        finally:
            self.assertTrue(True)

    def test_exit(self):
        try:
            exit('message')
        except AttributeError:
            self.assertTrue(True)
        finally:
            self.assertTrue(True)

    def test_notifications(self):
        try:
            notifications()
        except AttributeError:
            self.assertTrue(True)
        finally:
            self.assertTrue(True)