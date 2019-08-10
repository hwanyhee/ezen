from contacts.controller import ContactsController
from contacts.model import  ContactsModel
if __name__ == '__main__':
    #컨트롤러 인스턴스화
    ctrl = ContactsController()
    ctrl.run()