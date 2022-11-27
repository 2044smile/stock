# stock
I use Django, Slack, Telegram and get stock information

## Telegram
1. Telethon 
   1. 기존 채팅방의 대화를 가져오려고 하려면 token 키가 있어야 한다.
2. python-telegram-bot
   1. Add the bot to the desired group as administrator

# env
1. Poetry
   1. poetry install
   2. poetry run python manage.py runserver 0.0.0.0:8000
2. Docker
   1. docker build -t stock .
   2. docker run -it -p 8000:8000 --name container -v /Users/cslee/vscode/stock:/code/ stock
      1. -v(볼륨) 옵션 : 코드가 수정되면 감지하고 재시작