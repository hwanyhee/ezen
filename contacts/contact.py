class Contact:
    def __init__(self,name,phone,email,addr):
        self.name=name;
        self.phone = phone
        self.email = email
        self.addr = addr
    def toString(self):
        return 'name:{}\nphone:{}\nemail:{}\naddress:{}\n'.format(self.name,self.phone,self.email,self.addr)