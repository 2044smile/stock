# stock
I use Django, Slack, Telegram and get stock information

## Plan
1. Telethon 에서 텔레그램 채팅 가져오기 (O)
2. django-telethon use [stackoverflow](https://stackoverflow.com/questions/68976078/using-telethon-with-a-django-application)

## django-telegram
### problem
~~1. 휴대폰 인증번호 없이 진행 되는 법 or 인증을 받지않고 지속적인 연결~~<br>
   ~~* 현재는 휴대폰에서 인증번호를 받으면 값을 변경해서 실행하고 있음~~<br>
**<span style="color:red;">서버가 종료되지 않으면 재인증은 필요없음**<br>
~~2. 네이버 카페~~<br>
   ~~* 네이버 카페에 가입해야만 보이는 정보들이 존재함~~<br>
**<span style="color:red;">가입을 안해도 되는 링크로 대체**<br>
<br>
**3. 비동기로 텔레그램의 데이터를 실시간으로 가져올 수 있어야 한다.**
<br>~~* 3-1. Redis [poetry add redis]~~
<br>~~* 3-2. Celery [poetry add Celery]~~
<br>3-3. apscheduler [poetry add apscheduler 데이터 apscheduler 로 들어오는 것은 확인
<br>3-4. nohup poetry run python get_telethon.py &

**4. message.media.webpage.photo**
<br>How do I use photo file_reference <br>
Link: [stackoverflow](https://stackoverflow.com/questions/62391946/how-to-download-images-to-my-local-pc-using-telethon)



**4. 이상한 오류가 나오는지 수시로 확인**
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

<br>
<br>
<br>
<br>
<br>
<h3>20221226<br>
I had a problem but I solved it.<br>
Let us start again.
</h3>