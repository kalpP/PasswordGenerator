# Copying passwords to user's clipboard
import pyperclip

# Creating table
from tabel import Tabel

# Libraries that come with python3
import random
from getpass import getpass
import json
import os
import time
import hashlib

from pathlib import Path
from dotenv import load_dotenv, set_key

firstLogin = True

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
SALT = os.getenv("SALT")

def ClearTerminal():
    # Windows
    if(os.name == 'nt'):
        _ = os.system('cls')
    # Mac and Linux
    else:
        _ = os.system('clear')

def GetData():
    data = {}
    # Read the data.json file and save info into a dictionary called 'data'
    with open('data.json') as infile:
        data = json.load(infile)
    return data

def StoreData(website_name, user_id, user_pass, user_note):
    try:
        data = GetData()
    except:
        data = {}
    if(website_name not in data.keys()):
        data[website_name] = {user_id: [user_pass, user_note]}
    else:
        if(user_id in data[website_name]):
            print('This account has already been added!', end = ' ')
            overrideData = YesNoQuestion('Override account information?')
            if(not overrideData):
                return
        data[website_name][user_id] = [user_pass, user_note]
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True)

def GenerateRandomPassword():
    includeSpecialChar = YesNoQuestion('Include special characters?')
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
        elif(includeSpecialChar):
            password += special_char[random.randint(0, len(special_char) - 1)]
    if(len(password) > 0):
        pyperclip.copy(password)
        print('Copied password to clipboard!')
    return password

def encryptPassword(password):
    pass

def decryptPassword(password):
    pass

def encryptNote(password):
    pass

def decryptNote(password):
    pass

def AddAccount():
    # Name, UserId/Email, Password
    website_name = input('Name / URL: ').lower()
    user_id = input('UserID / EmailID: ').lower()
    user_pass = getpass(prompt = 'Password (--generate to assign random passowrd): ')
    if(user_pass == '--generate'):
        user_pass = GenerateRandomPassword()
    user_note = input('Notes (Press ENTER to skip) ')
    StoreData(website_name, user_id, user_pass, user_note)

def SearchPassword():
    pass

def ShowAllPasswords():
    try:
        data = GetData()
        # website Name, user ID, user Password, user Note
        website_arr, userId_arr, userPass_arr, userNote_arr = [], [], [] ,[]
        for website in data.keys():
            for user in data[website].keys():
                website_arr.append(website)
                userId_arr.append(user)
                '''
                # Display password in the table
                userPass_arr.append(data[website][user][0])
                '''
                userPass_arr.append('*' * (random.randint(6,12)))
                userNote_arr.append(data[website][user][1])
        table = Tabel([website_arr, userId_arr, userPass_arr, userNote_arr], columns = ["Website", "UserID", "Password", "Note(s)"])
        print(table)
    except:
        print('No data available.')

def YesNoQuestion(question):
    result = input(f'{question} (y/n)? ')
    while(result.lower() not in ['y', 'n']):
        print(f'Invalid input!')
        result = input(f'{question} (y/n)? ')
    return True if result.lower() == 'y' else False

def GetAction():
    action = input('Select a command (a - add / s - search / all - show all / g - generate password / c - clear / q - quit): ')
    while(action.lower() not in ['a','s','all','g','c','q']):
        print('Invalid input!')
        action = input('Select a command (a - add / s - search / all - show all / g - generate password / c - clear / q - quit): ')
    return action

def DeleteAllData():
    if(os.path.exists('data.json')):
        os.remove('data.json')

def HashPassword(password):
    hashed = hashlib.pbkdf2_hmac('sha256', bytes(password, encoding='utf-8'), bytes(SALT, encoding='utf-8'), 100000)
    return(hashed.hex())

def SetNewPassword():
    new_password = getpass('New Master Password: ')
    confirm_password = getpass('Confirm Password: ')
    if(HashPassword(new_password) == HashPassword(confirm_password)):
        set_key(env_path, "MASTER_PASSWORD", f"{HashPassword(new_password)}")
        print('Password changed!')
        return True
    print('Please try again later...')
    return False

def ChangeMasterPassword():
    incorrect_guesses = 0
    master_password = getpass('Current Master Password: ')
    master_password = HashPassword(master_password)
    while(incorrect_guesses < 4):
        if(master_password != os.getenv("MASTER_PASSWORD")):
            incorrect_guesses += 1
            print(f'Incorrect password! {5 - incorrect_guesses} attempts remaining..')
            master_password = getpass('Current Master Password: ')
            master_password = HashPassword(master_password)
        else:
            if(SetNewPassword()):
                print('Please restart the program!\n\n')
                exit(0)
    print('Please try again later...')
    return False

def ValidateUser():
    global firstLogin
    incorrect_guesses = 0
    master_password = getpass('Master Password (--r to reset): ')
    if(master_password == "--r"):
        ChangeMasterPassword()
    master_password = HashPassword(master_password)
    while(incorrect_guesses < 4):
        if(master_password != os.getenv("MASTER_PASSWORD")):
            incorrect_guesses += 1
            print(f'Incorrect password! {5 - incorrect_guesses} attempts remaining..')
            master_password = getpass('Master Password (--r to reset): ')
            if(master_password == "--r"):
                ChangeMasterPassword()
            master_password = HashPassword(master_password)
        else:
            firstLogin = False
            main()
    DeleteAllData()
    return False
    
def main():
    if(firstLogin):
        allow_access = ValidateUser()
        if(not allow_access):
            exit(0)
    action = GetAction()
    if(action == 'q'):
        print('\n\n')
        exit(0)
    elif(action == 'a'):
        AddAccount()
        print('\n')
    elif(action == 's'):
        SearchPassword()
        print('\n')
    elif(action == 'all'):
        ShowAllPasswords()
        print('\n')
    elif(action == 'g'):
        GenerateRandomPassword()
    elif(action == 'c'):
        ClearTerminal()
        print('\n')
    main()

if __name__ == "__main__":
    main()