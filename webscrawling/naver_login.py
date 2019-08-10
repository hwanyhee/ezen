from bs4 import BeautifulSoup
from selenium import webdriver

class NaverLogin:
    def __init__(self,url):
        self.driver = webdriver.Chrome('./driver/chromedriver')
        self.driver.implicitly_wait(3)
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')
    def autoLogin(self):
        self.driver.find_element_by_name('id').send_keys('아이디')
        self.driver.find_element_by_name('pw').send_keys('비밀번호')
        self.driver.implicitly_wait(3)

        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(3)

        self.driver.get('http://order.pay.naver.com/home')
        html =self.driver.page_source
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        notices = soup.select('div.p_inr > div.p_info> a >span')

        for i in notices:
            print(i.text.strip())