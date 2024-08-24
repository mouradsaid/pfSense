import wmi
from pystyle import *
from termcolor import colored
import colorama
import getpass
from cryptography.fernet import Fernet
import os

# def get_path_file():
#     file_path = str(os.path.abspath(__file__)).split('\\')
#     del file_path[-1]
#     file_path='//'.join(file_path)
#     return str(file_path)

key="FMrJg1Ujg-O2dOaE9LdTQNWd2g9cGVlEMUZ5U="

def encrypt_data(key,data):
    c = wmi.WMI()
    for bios in c.Win32_BIOS():
        serial=bios.SerialNumber
    all_data=f"{serial}-(*ps*)-{data}"
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(all_data.encode())
    with open('data.inc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

banner = Center.XCenter(
"""
# ********************************************************#
#                 __  __ ___ ____  _____ ____             #
#                |  \/  |_ _|  _ \| ____/ ___|            #
#                | |\/| || || |_) |  _| \___ \            #
#                | |  | || ||  _ <| |___ ___) |           #
#                |_|  |_|___|_| \_\_____|____/            #
#                                                         #   
#                          ConfBackup                     # 
#                                                         #                      
#*********************************************************#
                        
""")
print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))

menu=colored("""
The tool requires the router passwort 

[1] Enter the router passwort           
[2] Change the password
[3] menu
[4] Exit
""","cyan")
print(menu)


while True:
    choice = input(colored("Please select an option (1/2/3/4): ", 'magenta'))
    if choice == '1':
        print(colored("(If the router does not have a passwort leave it blank)", 'yellow'))
        password = getpass.getpass(colored("Enter the router password : ", 'blue'))
        encrypt_data(key,password)
        print(colored("The password has been saved", 'green'))
    elif choice == '2':
        new_password = getpass.getpass(colored("Enter the new router password: ", 'blue'))
        encrypt_data(key,new_password)
        print(colored("The password has been saved", 'green'))
    elif choice == '3':
        print(menu)
    elif choice == '4':
        print(colored("Exiting...", 'red'))
        break 
    else:
        print(colored("Invalid choice, please try again.", 'red'))

colorama.deinit()