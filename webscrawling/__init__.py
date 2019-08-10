from webscrawling.controller import Controller
if __name__ == '__main__':
    print('a.국회 크롤링')
    print('b.벅스 크롤링')
    print('f.네이버 크ㄹ로링')

    print('0.종료')
    menu = input('메뉴선택?\n')
    ctrl = Controller()
    ctrl.exec(menu)

