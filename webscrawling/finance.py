from bs4 import BeautifulSoup
from urllib.request import urlopen
class FinanceCrawler:
    def __init__(self,url):
        self.url=url
    def scrap(self):
        html = urlopen(self.url).read()
        soup = BeautifulSoup(html, 'html.parser')
        txt = soup.find(id='KOSPI_now').text
        print(txt)