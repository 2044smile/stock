import os

from bs4 import BeautifulSoup


class PresidentNewsroomCrawling:
    def __init__(self):
        print('__init__')

        self.president_newsroom_url = 'https://www.president.go.kr/newsroom'
        self.president_newsroom_fact_url = 'https://www.president.go.kr/newsroom/fact/'
        self.president_newsroom_briefing_url = 'https://www.president.go.kr/newsroom/briefing/'
        self.headers = {"Content-Type": "application/json"}
        

    def crawler(self, target):
        if target == 'fact':
            html = self.president_newsroom_fact_url
        elif target == 'briefing':
            html = self.president_newsroom_briefing_url

        soup = BeautifulSoup(html.text, 'html.parser')
