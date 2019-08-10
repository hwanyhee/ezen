from webscrawling.controller import Controller
if __name__ == '__main__':
    print('a.국회 크롤링')
    print('b.벅스 크ㄹ로링')

    print('0.종료')
    menu = int(input('메뉴선택?\n'))
    ctrl = Controller()
    ctrl.exec(menu)

