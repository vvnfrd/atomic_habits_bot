from rest_framework import serializers, request
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from habits.models import Habit
from habits.validators import TimeToCompleteValidator, PeriodicityValidator, IncompatibilityValidator, TimeValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ('id', 'place', 'time', 'action', 'pleasantly', 'associated_habit', 'periodicity', 'reward', 'time_to_complete', 'is_public')
        validators = [TimeToCompleteValidator(field='time_to_complete'),
                      PeriodicityValidator(field='periodicity'),
                      IncompatibilityValidator(fields=['associated_habit', 'reward', 'pleasantly']),
                      TimeValidator(field='time')]

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()

        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance