from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory

from habits.models import Habit
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            email='habit_tester@gmail.com',
            password='13799731'
        )

    def test_create_habits(self):

        """Тестирование функции создания привычки"""

        view = HabitCreateAPIView.as_view()
        request = self.factory.post('/habit/create/', {'action': 'test_create_habit'})
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_habits(self):

        """Тестирование функции просмотра привычек"""

        habit = Habit.objects.create(
            action='test_list_habit',
            time='12:00:00',
            time_to_complete='00:02:00',
            user=self.user
        )

        view = HabitListAPIView.as_view()
        request = self.factory.get('/habit/')
        force_authenticate(request, user=self.user)
        response = view(request)
        result = [{'id': habit.id, 'place': None, 'time': '12:00:00', 'action': 'test_list_habit', 'pleasantly': False,
                   'associated_habit': None, 'periodicity': 1, 'reward': None,
                   'time_to_complete': '00:02:00', 'is_public': False}]
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(response.data['results'], result)

    def test_retrieve_habit(self):

        """Тестирование функции просмотра привычки"""

        view = HabitRetrieveAPIView.as_view()

        habit = Habit.objects.create(
            action='test_retrieve_habit',
            time='12:00:00',
            time_to_complete='00:02:00',
            user=self.user
        )

        request = self.factory.get(f'lesson/{habit.pk}/')
        force_authenticate(request, user=self.user)
        response = view(request, pk=habit.id)

        result = {'id': habit.id, 'place': None, 'time': '12:00:00',
                  'action': 'test_retrieve_habit', 'pleasantly': False,
                  'associated_habit': None, 'periodicity': 1, 'reward': None,
                  'time_to_complete': '00:02:00', 'is_public': False}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, result)

    def test_update_habit(self):

        """Тестирование функции обновления привычки"""

        view = HabitUpdateAPIView.as_view()
        habit = Habit.objects.create(
            action='test_update_habit',
            time='14:00:00',
            time_to_complete='00:01:30',
            user=self.user
        )
        data = {'action': 'test_updated_lesson',
                'pleasantly': 'true'}
        request = self.factory.patch('lesson/update/', data=data)
        force_authenticate(request, user=self.user)
        response = view(request, pk=habit.id)
        result = {'id': habit.id, 'place': None, 'time': '14:00:00',
                  'action': 'test_updated_lesson', 'pleasantly': True,
                  'associated_habit': None, 'periodicity': 1, 'reward': None,
                  'time_to_complete': '00:01:30', 'is_public': False}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, result)

    def test_delete_habit(self):

        """Тестирование функции удаления привычки"""

        view = HabitDestroyAPIView.as_view()

        habit = Habit.objects.create(
            action='test_delete_habit',
            time='16:00:00',
            time_to_complete='00:01:50',
            user=self.user
        )
        before = Habit.objects.filter(action='test_delete_habit').exists()
        request = self.factory.delete('habit/')
        force_authenticate(request, user=self.user)
        response = view(request, pk=habit.id)
        after = Habit.objects.filter(action='test_delete_habit').exists()
        self.assertTrue(before)
        self.assertFalse(after)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
