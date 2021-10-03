import random
personalisation = []
option=input('would u like to create or read or update or delete: ')
i=1

class person():

    def __init__(self):
        pass


    def create(self, name, last_name, ID):
        self.name = name
        self.last_name = last_name
        self.ID = ID

    def read(self, ID_read):
        self.ID_read=ID_read



    def update(self, IDtoupdate):
        self.IDtoupdate= IDtoupdate



    def show(self):
        pass






x=random.randint(10000000, 99999999)
if option == 'create':
    a=person()
    a.create(input('Name: '), input('Last name: '), 321)
    while a.name[0].upper() != a.name[0] or a.last_name[0].upper() != a.last_name[0]:
        print("Invalid name: first letter needs to be an upper letter")
        a=person(input('Name: '), input("last name: "), 321)
    personalisation.append(a)
    print(personalisation[0].ID)
    option=input('would u like to create or read or update or delete: ')


if option == 'read':
    a.read(input('ID: '))
    print(personalisation.index('Adem'))
        
    