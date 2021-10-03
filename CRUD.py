import math
import random
Name_List=[]
Lastname_List=[]
ID_List=[]
a=1
a="adem"
print(type(a))

while a>0:
    Option=input('whould you like to create or read or update or delete? : ')
    if Option=="create":
        name_create=input('please enter your name: ')
        while name_create[0] != name_create[0].upper():
            print('The first character of your name has to be upper case')
            name_create = input('please enter your name: ')
        lastname_create=input('please enter your last name: ')
        while lastname_create[0] != lastname_create[0].upper():
            print('The first character of your name has to be have upper case')
            lastname_create=input('please enter your last name: ')
        x=random.randint(10000000,99999999)
        print(x)
        while x in ID_List:
            x=random.randint(10000000,99999999)
        Name_List.append(name_create)
        Lastname_List.append(lastname_create)
        ID_List.append(x)

    print(ID_List)

    if Option=="read":
        ID_read=input('please enter your existing ID: ')
        print(ID_read)
        while a>0:
            if type(ID_read) != int:
                print("Invalid ID")
                ID_read=input('please enter your existing ID: ')
            elif ID_read in ID_List:
                print(Name_List[ID_List.index(ID_read)], Lastname_List[ID_List.index(ID_read)])
                continue
            else:
                print('invalid ID')

    if Option=="update":
        ID_readtoUpdate=int(input('please enter your existing ID: '))
        if ID_readtoUpdate in ID_List:
            print(Name_List[ID_List.index(ID_readtoUpdate)], Lastname_List[ID_List.index(ID_readtoUpdate)])
            name_change=input('Please enter your name: ')
            while name_change[0].upper() != name_change[0]:
                print('Invalid name')
                name_change=input('Please enter your name:')
            lastname_change=input('Please enter your last name: ')
            while lastname_change[0].upper() != lastname_change[0]:
                print('Invalid Last name')
                lastname_change=input('Please enter your last name: ')
            Name_List[ID_List.index(ID_readtoUpdate)]= name_change
            Lastname_List[ID_List.index(ID_readtoUpdate)]= lastname_change
            continue

        else:
            print('invalid ID')


    if Option == "delete":
        ID_ReadtoDelete=int(input('Please enter your existing ID: '))
        if ID_ReadtoDelete in ID_List:
            print(Name_List[ID_List.index(ID_ReadtoDelete)], Lastname_List[ID_List.index(ID_ReadtoDelete)])
            Verification=input('are you sure you want to delete this? yes/no: ')
            Ver=['yes', 'no']
            while a>0:
                if Verification == 'yes':
                    Name_List.remove(Name_List[ID_List.index(ID_ReadtoDelete)])
                    Lastname_List.remove(Lastname_List[ID_List.index(ID_ReadtoDelete)])
                    ID_List.remove(ID_ReadtoDelete)
                elif Verification == 'no':
                    continue
                else:
                    print('Invalid answer')
                    Verification=input('are you sure you want to delete this? yes/no: ')
        else:
            print("Invalid ID")





a="adem"
print(type(a))










