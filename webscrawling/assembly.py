from bs4 import BeautifulSoup
from urllib.request import url

class AssemplyCrawler:
    def __init__(self,param):
        self.param=param
    def scrap(self):

        html = url.urlopen(self.param).read()
        soup = BeautifulSoup(html,'html.parser')
        txt = soup.find(id='summaryContentDiv').text
        print(txt)