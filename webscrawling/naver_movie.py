from bs4 import BeautifulSoup
from selenium import webdriver

class NaverMovie:
    def __init__(self,url):
        self.driver = webdriver.Chrome('./driver/chromedriver')
        self.driver.get(url)
        self.soup= BeautifulSoup(self.driver.page_source,'html.parser')
    def scrap(self):
        html = self.soup.prettify()

        all_div = self.soup.find_all('div', {'class', 'tit3'})
        print(all_div)
        for i in [div.a.string for div in all_div]:
            print(i)
        self.driver.close()