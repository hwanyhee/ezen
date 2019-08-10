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

        #code.rename(columns={'날짜': 'Date', '종가': 'Value'}, inplace=True)
        code.columns =['Date','Stock','YesterDay','Time','High','Low','Volumn']
        #Date컬럼을 인덱스로 설정하기
        code = code.set_index("Date")
        #날짜(인덱스) 순으로 내림 차순
        code.sort_index(ascending=True,inplace=True)

        print('[NaN 삭제전]')
        print(code)

        code_dop_row=code.dropna(axis=0)
        print('[NaN 삭제후]')
        print(code_dop_row)

        #날짜가 겹치지 않게 잘보이도록 figsize=(10,4)사이즈 변경
        code_dop_row[['Stock']].plot(figsize=(10,4))
        plt.show()
        code_dop_row.to_csv(self.item+'.csv')