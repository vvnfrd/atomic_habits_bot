# ATOMIC_HABITS_BOT
SPA веб-приложение

В 2018 году Джеймс Клир написал книгу «Атомные привычки», 
которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 
Прочитав книгу, я впечатлился и решил реализовать трекер полезных привычек.

ПАРОЛИ ОТ ВСЕХ ЮЗЕРОВ: 13799731

После каждого пуша оставляю бэкап БД в fixtures/backup.json

Телеграм бот имеет возможность авторизироваться в DRF и оставлять свой tg_id в моделях Users,
позволяющий рассылать уведомления когда нужно делать привычку.

Алгоритм включения:

python manage.py runserver,
redis-cli / redis-server,
python manage.py start_bot,
celery -A config worker -l INFO -P eventlet,
celery -A config beat -l INFO

tg bot:

https://t.me/HabitsSkyCourseBot