import datetime
import calendar
from habits.models import Habit
from users.models import User
from celery import shared_task
from bot.main_bot import bot


@shared_task
def notifications():
    print('opa')
    habits_list = []
    telegram_users = []
    for user in User.objects.all():
        if user.telegram_id is not None:
            telegram_users.append(user)

    for user in telegram_users:
        habits_list.append(
            {"telegram_id": user.telegram_id,
             "habits": list(Habit.objects.filter(user=user))}
        )
    for habits in habits_list:
        telegram_id = habits['telegram_id']
        for habit in habits['habits']:
            datetime_now = datetime.datetime.now()
            tmp_val = habit.time.split(':')
            task_time = datetime.time(hour=int(tmp_val[0]), minute=int(tmp_val[1]), second=int(tmp_val[2]))
            periodicity = habit.periodicity
            time_now = datetime_now.time()

            if habit.next_action is None:
                habit.next_action = datetime_now.replace(hour=task_time.hour,
                                                         minute=task_time.minute,
                                                         second=task_time.second,
                                                         microsecond=0)
                habit.save()

            while True:

                next_action = habit.next_action
                if task_time < time_now and datetime_now.day == next_action.day:
                    if habit.place is None and habit.reward is None:
                        text = f'Пора {habit.action.lower()}!'
                    elif habit.place is None and habit.reward is not None:
                        text = f'Пора {habit.action.lower()}!\nНаграда: {habit.reward}'
                    elif habit.place is not None and habit.reward is None:
                        text = f'Пора {habit.action.lower()}!\nМесто: {habit.place}'
                    else:
                        text = f'Пора {habit.action.lower()}!\nМесто: {habit.place}\nНаграда: {habit.reward}'
                    bot.send_message(telegram_id, text)
                    try:
                        habit.next_action = habit.next_action.replace(day=habit.next_action.day + periodicity)
                        habit.save()
                    except ValueError:
                        days_in_month = calendar.monthrange(datetime_now.year, datetime_now.month)[-1]
                        if habit.periodicity == 1 or days_in_month - datetime_now.day >= 0:
                            habit.next_action = habit.next_action.replace(
                                day=periodicity - (days_in_month - datetime_now.day), month=next_action.month + 1)
                            habit.save()
                    finally:
                        break

                    habit_db = Habit.objects.get(id=habit.id)
                    habit_db.next_action = habit.next_action
                    habit_db.save()
