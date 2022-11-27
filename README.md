# stock
I use Django, Slack, Telegram and get stock information

# env
1. Poetry
   1. poetry install
   2. poetry run python manage.py runserver 0.0.0.0:8000
2. Docker
   1. docker build stock .
   2. docker run -it -p 8000:8000 --name container stock