from contacts.model import ContactsModel

'''
아래 컨틀로러에서 메뉴  출력부분 및 
사용자 입력부분이 빠지고
입력이면 입력용 
출력이면 출력용 모델 로직을 호출해야 함

'''
class ContactsController:
    def __init__(self):
        # 모델 인스턴스화
       self.model = ContactsModel()
    @staticmethod
    def menuPrint():
        print('1.입력')
        print('2.출력')
        print('3.삭제')
        print('4.수정')
        print('0.종료')
        menu =int(input('메뉴선택?\n'))
        return menu

    def run(self):
        contacts =[]
        while 1:
            menu = self.menuPrint()
            if menu ==1 :


                name = input('name?')
                phone = input('phone?')
                email = input('email?')
                addr = input('address?')
                contact=self.model.setContact(name, phone, email, addr)
                contacts.append(contact)
            elif menu ==2:
                print(self.model.getContact(contacts))
            elif menu ==3:
                name=input('삭제할 이름?')
                self.model.deleteContact(contacts,name)

            elif menu==0:
                print('프로그램을 종료합니다')
                break