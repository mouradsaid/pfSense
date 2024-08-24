from cryptography.fernet import Fernet
import configparser
import os
import paramiko
from datetime import datetime
import sys


if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

key="FMrJg1Ujg-O2dOaE9LdTQNWd2g9cGVlEMUZ5U="

def read_settings(file):
    config = configparser.ConfigParser()
    config.read(file)
    settings = {}
    for section in config.sections():
        settings[section] = {}
        for key in config[section]:
            settings[section][key] = config[section][key]
    return settings

try:
    cipher = Fernet(key)
    with open( os.path.join(current_dir, 'data.inc'), 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data).decode()

    settings = read_settings(os.path.join(current_dir, 'settings.ini'))
    hostname=settings['Pfsense']['ip']
    username=settings['Pfsense']['username']
    password=decrypted_data.split('-(*ps*)-')[1]
    remote_path=settings['Pfsense']['remote_path']
    local_path=settings['Pfsense']['local_path']

    now = datetime.now()

    year=str(now.year)
    day=str(now.day)
    month=str(now.month)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)

    if not os.path.isdir(f'{local_path}/{month}-{year}'):
        os.makedirs(f'{local_path}/{month}-{year}')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.get(remote_path, f'{local_path}/{month}-{year}/{day}  {hour}-{minute}-{second}.xml')
    sftp.close()
    ssh.close()
except Exception as e:
    pass 