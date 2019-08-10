from bs4 import BeautifulSoup
from urllib.request import urlopen

class AssemplyCrawler:
    def __init__(self,param):
        self.param=param
    def scrap(self):

        html =urlopen(self.param).read()
        soup = BeautifulSoup(html,'html.parser')
        txt = soup.find(id='summaryContentDiv').text
        print(txt)