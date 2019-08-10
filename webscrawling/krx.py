import pandas as pd

class Krxcrawler:

    def __init__(self,url):
        self.url=url
    def scrap(self):
        code = pd.read_html(self.url , header='0')[0]
        print(code)
