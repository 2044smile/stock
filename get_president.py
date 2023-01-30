import re, os, requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from datetime import datetime
from stock.models import PresidentFact

from bs4 import BeautifulSoup


class PresidentNewsroomCrawling:
    def __init__(self):
        print('__init__')
        
        self.link_url = []
        
        self.president_url = requests.get(url='https://www.president.go.kr')
        self.president_newsroom_url = requests.get(url='https://www.president.go.kr/newsroom')
        self.president_newsroom_fact_url = requests.get(url='https://www.president.go.kr/newsroom/fact/')
        self.president_newsroom_briefing_url = requests.get(url='https://www.president.go.kr/newsroom/briefing/')
        self.headers = {"Content-Type": "application/json"}
        

    def crawler(self, target):
        if target == 'fact':
            html = self.president_newsroom_fact_url
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
                    text = b.get_text().replace("\n", "").strip("복사확인").replace("\xa0", "")
                    
                    # 날짜 가져오기 after, save database
                    match = re.search(r'\d{4}.\d{2}.\d{2}', text)
                    date = datetime.strptime(match.group(), '%Y.%m.%d')  # match.group() 2023.01.27 to datetime

                    get_dates = re.sub(r'\d{4}.\d{2}.\d{2}', '', text)  # text 에서 날짜 제거
                    get_special_characters = get_dates.split('→')
                    get_links = get_special_characters[1].split('https://')[1].split('링크')[0]

                    PresidentFact.objects.update_or_create(
                        title=get_special_characters[0],
                        description=get_special_characters[1],
                        link=get_links,
                        date=date
                    )
            
        elif target == 'briefing':
            html = self.president_newsroom_briefing_url
        
p = PresidentNewsroomCrawling()
p.crawler('fact')