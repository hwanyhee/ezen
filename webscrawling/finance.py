from bs4 import BeautifulSoup
from urllib.request import urlopen
class FinanceCrawler:
    def __init__(self,url):
        self.url=url
    def scrap(self):
        html = urlopen(self.url).read()
        soup = BeautifulSoup(html, 'html.parser')
        kospi = soup.find(id='KOSPI_now').text
        kosdaq = soup.find(id='KOSDAQ_now').text
        print('코스피:{} 코스닥:{}'.format(kospi,kosdaq))