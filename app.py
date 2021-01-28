import random
import pyperclip
from getpass import getpass
global storage
storage = {}
    
def GenerateRandomPassword():
    includeSpecialChar = (YesNoQuestion('Include special characters?'))
    password_length = (random.randint(20, 50))
    password = ''
    for position in range(password_length):
        '''
        lowercase letter:  a-z          (3/10)
        uppercase letter:  A-Z          (3/10)
        number:            0-9          (2/10)
        special character: ! @ # ? ]    (2/10)
        '''
        special_char = '!@#?]'
        char_type = random.randint(1, 10)
        if(char_type >= 1 and char_type <= 3):
            password += chr(random.randint(97, 122))
        elif(char_type >= 4 and char_type <= 6):
            password += chr(random.randint(65, 90))
        elif(char_type == 7 or char_type == 8):
            password += chr(random.randint(48, 57))
        elif(includeSpecialChar == 'y'):
            password += special_char[random.randint(0, len(special_char) - 1)]
    if(len(password) > 0):
        pyperclip.copy(password)
        print(f'Password: {password}')
        print('Copied password to clipboard!')
    main()


def decrypt(password):
    pass

def encrypt(password):
    pass

def AddAccount():
    # Name, UserId/Email, Password
    name = input('Name / URL: ').lower()
    userID = input('UserID / EmailID: ').lower()
    userPass = getpass(prompt = 'Password: ')
    userNote = input('Notes (Press ENTER to skip) ')
    new_data = [userID, userPass, userNote]
    if(name in storage):
        storage[name].append(new_data)
    else:
        storage[name] = [new_data]
    main()

def SearchPassword():
    pass

def ShowAllPasswords():
    print(storage)
    main()

def YesNoQuestion(question):
    result = input(f'{question} (y/n)? ')
    while(result.lower() not in ['y', 'n']):
        print(f'Invalid input!')
        result = input(f'{question} (y/n)? ')
    return True if result.lower() == 'y' else False

def getAction():
    action = input('Select a command (a - add / s - search / all - show all / g - generate password / q - quit): ')
    while(action.lower() not in ['a','s','all','q']):
        print('Invalid input!')
        action = input('Select a command (a - add / s - search / all - show all / g - generate password / q - quit): ')
    return action

def main():
    action = getAction()
    if(action == 'q'):
        quit()
    elif(action == 'g'):
        GenerateRandomPassword()
    elif(action == 'a'):
        AddAccount()
    elif(action == 's'):
        SearchPassword()
    elif(action == 'all'):
        ShowAllPasswords()

if __name__ == "__main__":
    main()