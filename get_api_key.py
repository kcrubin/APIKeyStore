import pandas as pd
import csv
import sys
import DPAPI as dp
import win32crypt
import subprocess
import os

from cryptography.fernet import Fernet
input = "banana"
encrypted_data = win32crypt.CryptProtectData(input.encode(),None,None,None,None,0)
print(encrypted_data.decode())

#import dpapick as  dpick

with open('C:\\Users\PC\\.apikeys\\keys.csv','r',encoding='utf-8',errors='ignore') as f:
    data = csv.reader(f)
    d = {rows[0]:rows[1] for rows in data}

if (sys.argv[1] in d) ==True:
    key=sys.argv[1]
    value_in_dict = d[sys.argv[1]]
    #deptdata = value_in_dict.decode()
    print(type(value_in_dict))
    byte_data = bytes(value_in_dict,'utf-16')
    print(byte_data)
    decrypted_data = win32crypt.CryptUnprotectData(byte_data,None,None,None,0)[1].decode()
    #powershell_command = "[System.Runtime.InteropServices.Marshal]::PtrToStringBSTR([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR((ConvertTo-SecureString {})))".format(value_in_dict)
    #process = subprocess.check_output(powershell_command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #value =subprocess.check_output(['powershell',powershell_command]).decode()
    #print('Key:{}; Value:{}'.format(key,value))
    #stdout,stderr = process.communicate()
    #print(stdout)
    print(decrypted_data)
    
else:
    print('Key not found')
    

