from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, HabitPublicListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/', HabitListAPIView.as_view(), name='habit-list'),
    path('habits/public/', HabitPublicListAPIView.as_view(), name='habit-list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-info'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
