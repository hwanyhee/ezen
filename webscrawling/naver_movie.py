from bs4 import BeautifulSoup
from selenium import webdriver

class NaverMovie:
    def __init__(self,url):
        driver = webdriver.Chrome('./driver/chromedriver')
        driver.get(url)
        self.soup= BeautifulSoup(driver.page_source,'html.parser')
    def scrap(self):
        html = self.soup.prettify()
        print(html)