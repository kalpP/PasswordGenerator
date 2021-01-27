import random
import pyperclip

global password_manager
password_manager = {}

def StorePassword(websiteName, password):
    if(websiteName in password_manager):
        updatePassword = input(f'Do you want to update the password for {websiteName} (y/n)? ')
        while(includeSpecialChar.lower() not in 'yn'):
            print(f'Invalid Input! Please try again..')
            updatePassword = input(f'Do you want to update the password for {websiteName} (y/n)? ')
        if(updatePassword.lower() == 'y'):
            password_manager[websiteName] = encrypted_password(password)
            print('Password updated!')
        return
    password_manager[websiteName] = encryptPassword(password)
    print('Password saved!')
    return

def encryptPassword(password):
    encrypted_password = ''
    for letter in password:
        if(letter == ' '):
            encrypted_password += ' '
        else:
            encrypted_password += chr(ord(letter) + 7)
    return encrypted_password

def decryptPassword(password):
    decrypted_password = ''
    for letter in password:
        if(letter == ' '):
            decrypted_password += ' '
        else:
            decrypted_password += chr(ord(letter) - 7)
    return decrypted_password

def PasswordGenerator(includeSpecialChar):
    password_length = (random.randint(20, 50))
    password = ''
    for position in range(password_length):
        '''
        lowercase letter:  a-z          (3/10)
        uppercase letter:  A-Z          (3/10)
        number:            0-9          (2/10)
        special character: ! @ # ? ]    (2/10)
        '''
        special_char = '!@#?]%=+-_'
        char_type = random.randint(1, 10)
        if(char_type >= 1 and char_type <= 3):
            password += chr(random.randint(97, 122))
        elif(char_type >= 4 and char_type <= 6):
            password += chr(random.randint(65, 90))
        elif(char_type == 7 or char_type == 8):
            password += chr(random.randint(48, 57))
        elif(includeSpecialChar == 'y'):
            password += special_char[random.randint(0, len(special_char) - 1)]
    pyperclip.copy(password)
    spam = pyperclip.paste()
    return password

def main():
    includeSpecialChar = input('Do you want the password to include special characters (y/n)? ')
    while(includeSpecialChar.lower() not in 'yn'):
        print(f'Invalid input! Please try again..')
        includeSpecialChar = input('Do you want the password to include special characters (y/n)? ')
    password = PasswordGenerator(includeSpecialChar.lower())
    print(f'Your password is: {password}')
    print('Copied password to clipboard!')

    storePassword = input('Do you want the store the password (y/n)? ')
    while(includeSpecialChar.lower() not in 'yn'):
        print(f'Invalid input! Please try again..')
        storePassword = input('Do you want the store the password (y/n)? ')
    if(storePassword.lower() == 'y'):
        websiteName = input('What website is this password for? ')
        StorePassword(websiteName, password)
    
    for acc in password_manager:
        print(f'{acc} -- {password_manager[acc]}')

if __name__ == "__main__":
    main()