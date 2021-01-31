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
   MASTER_PASSWORD = "<your master password>"
   SALT = "<a random string>"
   ```
   NOTE: YOU NOT CHANGE YOUR SALT WITHOUT MANUALLY CHANGING MASTER_PASSWORD IN .ENV FILE
