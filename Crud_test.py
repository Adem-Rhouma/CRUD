import random

option=input('would u like to create or read or update or delete: ')
i=1
personalisation = []
class person():

    def __init__(self):
        pass


    def create(self, name, last_name, ID):
        self.name = name
        self.last_name = last_name
        self.ID = ID
        while name[0].upper() != name[0] or last_name[0].upper() != last_name[0]:
            print("Invalid name: first letter needs to be an upper letter")
            a.create(input('Name: '), input("last name: "), 321)
        print(ID)
        print(a.create)
        personalisation.append(a.create)
        print(personalisation[0].name)
        
        

    def read(self, ID_read):
        self.ID_read=ID_read
        print(personalisation[0].ID)
        b=personalisation.index(ID_read)
        print('test')
        print(b)



    def update(self, IDtoupdate):
        self.IDtoupdate= IDtoupdate



    def show(self):
        pass





a=person()
xlist=[]
x=random.randint(10000000, 99999999)
while x in xlist:
    x=random.randint(10000000, 99999999)
xlist.append(x)
if option == 'create':
    a.create(input('name: '), input('last name: '), 321)
    option=input('would u like to create or read or update or delete: ')

if option == 'read':
    a.read(input('ID: '))
        
    