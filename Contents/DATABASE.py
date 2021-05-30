#!/usr/bin/env python
import time
#ur mum

def selectstaff():
    print ('Please select staff')
    print ('[1]S3CR3T DEV(S3CR3TH4CK)')
    print ('[2]ForesterDev(Gon)')
    print ('[3]Quit')
    secret = input('Please enter your choice:')
    if secret == '1':
        print ('name:S3CR3T DEV')
        print ('username:S3CR3TH4CK')
        print ('discord tag:#5279')
        print ('role:admin')
        secretdev = input('Enter b to go back:')
        if secretdev == 'b':
            selectstaff()
        else:
            print ('wrong = close')
            exit
    elif secret == '2':
        print ('name:Gon(ForesterBlox)')
        print ('username:Gon')
        print ('discord tag:#9586')
        print ('role:designer/builder')
        gon = input('enter b to go back:')
        if gon == 'b':
            selectstaff()
        else:
            print ('wrong = close')
            exit
    elif secret == '3':
        menu()

def menu():
    print ('Welcome to STIX gang secret information')
    print ("Please don't tell these information to anyone!")
    print ('[1]Staff information')
    print ('[2]WIP game')
    print ('[3]Quit')
    choice = input('Please enter your choice: ')
    if choice == '1':
        selectstaff()
    elif choice == '2':
        print ('Current wip game:No Escape Z')
        print ('Plan:secret')
        print ('Developer team:ST1X STUDIO')
        print ('Class:Important')
        menub2 = input('Enter b to go back:')
        if menub2 == 'b':
            menu()
        else:
            print ('Error:failed 2 times')
            print ('closing...')
            exit()
    elif choice == '3':
        print ('closing...')
        time.sleep(2)
    else:
        print ("It's not a choice")
        menub = input('Enter b to enter choices again:')
        if menub == 'b':
            menu()
        else:
            print ('Error:failed 2 times')
            print ('closing...')
            time.sleep(2)

def passcode():
    passcode = input('Please enter STIX staff passcode:')
    if passcode == '3958':
        login()
    else:
        print ('WRONG NUMBER CLOSING SOFTWARE...')
        time.sleep(2)


def login():
    username = input('Please enter your username: ')
    if username == 'Gon':
        password = input('Please enter your password: ')
        if password == 'Yummycum3958':
            menu()
        else:
            print ('Incorrect password please enter password again')
            again = input('Enter b to enter password again: ')
            if again == 'b':
                login()
    elif username == 'S3CR3TH4CK':
        password2 = input('Please enter your password: ')
        if password2 == 'delooftoguoy':
            menu()
        else:
            print ('Incorrect password please enter your password again')
            again2 = input('Enter b to enter your password again: ')
            if again2 == 'b':
                login()
            else:
                failagain = input('PLease enter lowercase b: ')
                if failagain == 'b':
                    login()
                else:
                    print ('Error:failed 2 times')
                    print ('closing..')
                    time.sleep(2)
    else:
        print ('Incorrect username please enter username again')
        useragain2 = input('Enter b to enter your username again: ')
        if useragain2 == 'b':
            login()
        else:
            failagain2 = input('PLease enter lowercase b: ')
            if failagain2 == 'b':
                login()
            else:
                print ('Error:failed 2 times')
                print ('closing...')
                time.sleep(2)



















































































































































































































execute = passcode()
print (execute)