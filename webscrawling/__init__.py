from webscrawling.controller import Controller
if __name__ == '__main__':
    while True:
        print('a.국회 크롤링')
        print('b.벅스 크롤링')
        print('f.네이버 크롤링')
        print('k.KRX 크롤링')
        print('n.네이버 주식 크롤링')
        print('m.네이버 영화 크롤링')
        print('l.네이버 자동 로그인')
        print('0.종료')
        menu = input('메뉴선택?\n')
        if menu == '0':
            break
        ctrl = Controller()
        ctrl.exec(menu)

