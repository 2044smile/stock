# stock
I use Django, Slack, Telegram and get stock information

## Plan
1. Telethon 에서 텔레그램 채팅 가져오기 (O)
2. django-telethon use [stackoverflow](https://stackoverflow.com/questions/68976078/using-telethon-with-a-django-application)
3. bootstrap [url](https://django-bootstrap-v5.readthedocs.io/en/latest/quickstart.html)
4. [What is the most pythonic way to check if multiple variables are not None?](https://stackoverflow.com/questions/42360956/what-is-the-most-pythonic-way-to-check-if-multiple-variables-are-not-none)
5. Serializer and Swagger(drf-yasg) are introduction
6. Dumpdata & Loaddata
   1. Change HOST: DB to HOST: localhost
   2. poetry run python manage.py dumpdata --exclude auth.permission --exclude contenttypes > stock.json
   3. poetry run python manage.py loaddata stock.json
   4. Change HOST: localhost to HOST: DB
   5. Mac(로컬) 에서 접근보다 docker-compose exec -it web /bin/bash 를 사용할 것
7. I completed the kakao login and I think I'll make a jwt
8. I make a 'Kakao Login(kakao_nickname)' + put in another information(sex, age, Id...)

## django-telegram
### problem
~~1. 휴대폰 인증번호 없이 진행 되는 법 or 인증을 받지않고 지속적인 연결~~<br>
   ~~* 현재는 휴대폰에서 인증번호를 받으면 값을 변경해서 실행하고 있음~~<br>
**<span style="color:red;">서버가 종료되지 않으면 재인증은 필요없음**<br>
~~2. 네이버 카페~~<br>
   ~~* 네이버 카페에 가입해야만 보이는 정보들이 존재함~~<br>
**<span style="color:red;">가입을 안해도 되는 링크로 대체**<br>
**3. 비동기로 텔레그램의 데이터를 실시간으로 가져올 수 있어야 한다.**
<br>~~* 3-1. Redis [poetry add redis]~~
<br>~~* 3-2. Celery [poetry add Celery]~~
<br>3-3. apscheduler [poetry add apscheduler 데이터 apscheduler 로 들어오는 것은 확인
<br>3-4. nohup poetry run python get_telethon.py &
<br>4-1. Run time of job "job_am (trigger: cron[hour='14', minute='0,15,30,53', second='1'], next run at: 2023-01-17 14:00:01 KST)" was missed by 0:20:16.952368

**4. message.media.webpage.photo**

How do I use photo file_reference
Link: [stackoverflow](https://stackoverflow.com/questions/62391946/how-to-download-images-to-my-local-pc-using-telethon)

**5. nohup problem**

I use to 'nohup poetry run python get_telethon.py' in local but error by 'ModuleNotFoundError: No module named 'django.db.migrations.migration'
But I use to 'nohup poetry run python get_telethon.py' in docker-compose it's not error and I have to check it out tomorrow

## env
1. Poetry
   1. poetry install
   2. poetry add 
   3. poetry run python manage.py runserver 0.0.0.0:8000
2. ~~Docker~~
   1. ~~docker build -t stock .~~
   2. ~~docker run -it -p 8000:8000 --name container -v /Users/cslee/vscode/stock:/code/ stock~~
      1. ~~-v(볼륨) 옵션 : 코드가 수정되면 감지하고 재시작~~
      2. ~~-e(environment) *옵션 : 중요~~
3. Docker-compose
   1. docker-compose up -d --build
   2. and a m1 mac 'platform: linux/amd64' in docker-compose
   3. env_file ./.env and set ${POSTGRES_DATABASE}
4. django-environ
   1. 
   ```
   import environ
   env = environ.Env(DEBUG=(bool, True))
   environ.Env.read_env(
      env_file=os.path.join(BASE_DIR, '.env')
   )

   SECRET_KEY = env('SECRET_KEY')
   and
   Don't ever use 'space bar'
   A = 'A' (x)
   A='A' (O)
   ```

## Reference
- https://docs.telethon.dev/en/stable/index.html

<br>
<br>
<br>
<br>
<br>
<br>
<h3>20221226<br>
I had a problem but I solved it.<br>
Let us start again.
</h3>
