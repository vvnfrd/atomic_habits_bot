import datetime

from rest_framework.serializers import ValidationError


class TimeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        if 'time' in value:
            try:
                tmp_val = dict(value).get(self.field)
                print(value)
                tmp_val = tmp_val.split(':')
                time = datetime.timedelta(hours=int(tmp_val[0]), minutes=int(tmp_val[1]), seconds=int(tmp_val[-1]))

                if len(tmp_val) != 3:
                    raise ValidationError('Время выполнения должно быть в формате "HH:MM:SS"')

            except ValueError:
                raise ValidationError('Время выполнения должно быть в формате "HH:MM:SS"')
            except IndexError:
                raise ValidationError('Время выполнения должно быть в формате "HH:MM:SS"')

class TimeToCompleteValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        if 'time_to_complete' in value:
            try:
                tmp_val = dict(value).get(self.field)
                print(value)
                tmp_val = tmp_val.split(':')
                time_to_complete = datetime.timedelta(hours=int(tmp_val[0]), minutes=int(tmp_val[1]), seconds=int(tmp_val[-1]))

                if len(tmp_val) != 3:
                    raise ValidationError('Время выполнения должно быть в формате "HH:MM:SS"')

                if not time_to_complete <= datetime.timedelta(minutes=2):
                    raise ValidationError('Время выполнения должно быть меньше 2 минут.')
            except ValueError:
                raise ValidationError('Время выполнения должно быть в формате "HH:MM:SS"')
            except IndexError:
                raise ValidationError('Время выполнения должно быть в формате "HH:MM:SS"')


class PeriodicityValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        if 'periodicity' in value:
            tmp_val = dict(value).get(self.field)

            if tmp_val > 7 or tmp_val < 0:
                raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


class IncompatibilityValidator:
    def __init__(self, fields):
        self.fields = fields # fields = ['associated_habit', 'reward', 'useful_bonus']

    def __call__(self, value):

        if 'associated_habit' in value or 'reward' in value or 'pleasantly' in value:
            print(self.fields)
            # print(self.request.user)
            if dict(value).get('associated_habit') != None and dict(value).get('reward') != None:
                raise ValidationError("Не должно быть заполнено одновременно и поле вознаграждения, "
                                      "и поле связанной привычки. Можно заполнить только одно из двух полей.")

            if dict(value).get('associated_habit'):
                associated_habit = dict(value).get('associated_habit')
                if not associated_habit.pleasantly:
                    raise ValidationError("В связанные привычки могут попадать "
                                          "только привычки с признаком приятной привычки.")

            if dict(value).get('pleasantly') and dict(value).get('reward') or dict(value).get('associated_habit'):
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")