import os, requests

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
        elif target == 'briefing':
            html = self.president_newsroom_briefing_url

        soup = BeautifulSoup(html.text, 'html.parser')
        bs = soup.select(
            "body > div.container > div > section.fact > div > div > a"
        )
        for b in bs:
            self.link_url.append(self.president_url.url.rstrip('/') + b.get('href'))
        
        print(self.link_url)
        
p = PresidentNewsroomCrawling()
p.crawler('fact')