import re, os, requests, time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from datetime import datetime
from stock.models import PresidentFact

from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler


class PresidentNewsroomCrawling:
    def __init__(self):
        self.link_url = []
        
        self.president_url = requests.get(url='https://www.president.go.kr')
        self.president_newsroom_url = requests.get(url='https://www.president.go.kr/newsroom')
        self.president_newsroom_fact_url = requests.get(url='https://www.president.go.kr/newsroom/fact/')
        self.president_newsroom_briefing_url = requests.get(url='https://www.president.go.kr/newsroom/briefing/')
        self.headers = {"Content-Type": "application/json"}
        

    def crawler(self, target):
        if target == 'fact':
            html = self.president_newsroom_fact_url  # requests.get
            soup = BeautifulSoup(html.text, 'html.parser')
            bs = soup.select(
                "body > div.container > div > section.fact > div > div > a"
            )
            for b in bs:
                self.link_url.append(self.president_url.url.rstrip('/') + b.get('href'))

                for url in self.link_url:                
                    html = requests.get(url=url)
                    soup = BeautifulSoup(html.text, 'html.parser')
                    bs = soup.select(
                        "body > div.container > div > section.view_area"
                    )

                    for b in bs:
                        text = b.get_text().replace("\n", "").strip("복사확인").replace("\xa0", "")  # 필요없는 문자 제거
                        
                        match = re.search(r'\d{4}.\d{2}.\d{2}', text)  # text 에서 날짜 까내기
                        date = datetime.strptime(match.group(), '%Y.%m.%d')  # match.group() 2023.01.27 to datetime 으로 만들기
                        remove_dates = re.sub(r'\d{4}.\d{2}.\d{2}', '', text)  # text 에서 날짜 제거

                        get_info = remove_dates.split('→')

                        get_title = get_info[0]
                        get_description = get_info[1].split("목록")[0]
                        get_link = get_info[1].split("목록")[1].split("링크")[0]

                        PresidentFact.objects.update_or_create(
                            title=get_title,
                            description=get_description,
                            link=get_link,
                            date=date
                        )
        elif target == 'briefing':
            html = self.president_newsroom_briefing_url


if __name__ == '__main__':
    sched = BackgroundScheduler(timezone="Asia/Seoul")
    sched.start()

    while True:
        @sched.scheduled_job('cron', hour='15', minute='0', second='1', misfire_grace_time=None)
        def job_am():
            p = PresidentNewsroomCrawling()
            p.crawler('fact')

        time.sleep(1)
