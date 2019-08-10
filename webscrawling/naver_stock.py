#https://finance.naver.com/item/sise_day.nhn?code=005930
import pandas as pd
import matplotlib.pyplot as plt

class NaverStock:
    def __init__(self,item):
        self.item=item
    def scrap(self):
        url = 'https://finance.naver.com/item/sise_day.nhn?code={}'.format(self.item)
        #class="tah p11"
        code = pd.read_html(url, header=0)[0]
        cols = list(code.columns)
        print(cols)
        #컬럼명 바꾸기

        code.rename(columns={'날짜': 'Date', '종가': 'Value'}, inplace=True)

        print('[NaN 삭제전]')
        print(code)

        code_dop_row=code.dropna(axis=0)
        print('[NaN 삭제후]')
        print(code_dop_row)

        code_dop_row[['Date', 'Value']].plot()
        plt.show()
        code_dop_row.to_csv(self.item+'.csv')