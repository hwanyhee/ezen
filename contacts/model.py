from contacts.contact import Contact
class ContactsModel:
    def __init__(self):
       pass

    @staticmethod
    def setContact(name,phone,email,addr):
        contact =Contact(name,phone,email,addr)
        return contact
    @staticmethod
    def getContact(params):
        contacts=[]
        for contact in params:
            contacts.append(contact.toString())
        return ''.join(contacts)
    @staticmethod
    def deleteContact(params,name):
        for index,contact in enumerate(params):
            if contact.name==name:
                del params[index]

