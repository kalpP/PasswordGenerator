# Set-Up
1. To install the requirements, type the following into your terminal:
   ```
   # For Python2
   pip install -r requirements.txt
   
   # For Python3
   pip3 install -r requirements.txt
   ```
   
# To set a master password
1. Create a .env file in the same directory as the project
2. The content of the .env file should be:
   ```
   # NOTE: ORIGINAL PASSWORD WILL BE AN EMPTY STRING ['']
   MASTER_PASSWORD = "0ff5a7e4bd2ce271a4e38b3fb2fa75085763d0bcc8527d77d0581b6d8f24aa48"
   
   # NOTE: YOU NOT CHANGE YOUR SALT WITHOUT MANUALLY CHANGING MASTER_PASSWORD IN .ENV FILE
   SALT = "<a random string>"
   ```
