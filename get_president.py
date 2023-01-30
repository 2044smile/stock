import re
import os, requests
from datetime import datetime

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

            text_lst = []
            
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
                    remove_date = re.sub(r'\d{4}.\d{2}.\d{2}', '', text)  # text 에서 날짜 제거
                    
                    # special characters 제거 to List
                    remove_special_characters = remove_date.split('→')
                    # print(remove_special_characters[0])  # title
                    # print(remove_special_characters[1])  # description

                    import pdb;
                    pdb.set_trace()
                    remove_links = remove_special_characters.split('https://')[1].split("링크")[0]
                    print(remove_links) 
            
        elif target == 'briefing':
            html = self.president_newsroom_briefing_url
        
p = PresidentNewsroomCrawling()
p.crawler('fact')