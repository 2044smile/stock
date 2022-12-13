# stock
I use Django, Slack, Telegram and get stock information

## Plan
1. Telethon 에서 텔레그램 채팅 가져오기 (O)
2. django-telethon use (ing)[https://stackoverflow.com/questions/68976078/using-telethon-with-a-django-application]

## Telegram

## env
1. Poetry
   1. poetry install
   2. poetry run python manage.py runserver 0.0.0.0:8000
2. Docker
   1. docker build -t stock .
   2. docker run -it -p 8000:8000 --name container -v /Users/cslee/vscode/stock:/code/ stock
      1. -v(볼륨) 옵션 : 코드가 수정되면 감지하고 재시작
      2. -e(environment) 옵션 : 중요

## Reference
- https://docs.telethon.dev/en/stable/index.html