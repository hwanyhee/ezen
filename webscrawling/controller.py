from webscrawling.assembly import AssemplyCrawler
from webscrawling.bugsmusic import  BugsCrawler
from webscrawling.finance import FinanceCrawler
from webscrawling.krx import  Krxcrawler
from webscrawling.naver_stock import NaverStock
from webscrawling.naver_movie import NaverMovie
class Controller:
    def __init__(self):
        pass
    def exec(self,flag):
        if flag=='a':
            a = AssemplyCrawler('http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7')
            a.scrap()
        elif flag=='b':
            b = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11')
            b.scrap()
        elif flag=='f':
            f = FinanceCrawler('https://finance.naver.com/sise/')
            f.scrap()
        elif flag=='k':
            k = Krxcrawler('http://kind.krx.co.kr/disclosureSimpleSearch.do?method=disclosureSimpleSearchMain')
            k.scrap()
        elif flag=='n':
            code = input('상장코드값?')
            n = NaverStock(code)
            n.scrap()
        elif flag == 'm':
            m = NaverMovie('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
            m.scrap()

