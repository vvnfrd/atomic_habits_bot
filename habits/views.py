from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner

"""CRUD Habit"""


class HabitCreateAPIView(generics.CreateAPIView):
    """Create a habit"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # data = request.data
        # data['user'] = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            new_habit = serializer.save()
            new_habit.user = self.request.user
            new_habit.save()
        except ValueError:
            pass


class HabitListAPIView(generics.ListAPIView):
    """Get habit's list"""
    request = {}
    user = {}
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get(self, request, *args, **kwargs):
        self.request = request
        self.user = request.user
        return self.list(request, *args, **kwargs)

    def get_queryset(self):

        print(type(Habit.objects.filter(user=self.request.user)))
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Get public habit's list"""
    request = {}
    user = {}
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get(self, request, *args, **kwargs):
        self.request = request
        self.user = request.user
        return self.list(request, *args, **kwargs)

    def get_queryset(self):

        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Get detail info about habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Update habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    # def put(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     return self.partial_update(request, *args, **kwargs)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Delete habit"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
