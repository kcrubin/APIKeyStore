import csv
import os
import shutil

username = os.getlogin() ##fetch username
api_key_path = f'C:\\Users\\{username}\\.apikeys'

header = ['Key','Value']

with open(api_key_path + '\\keys.csv','w', encoding='UTF8',newline='') as keyfile:
    writer = csv.writer(keyfile)
    #filewriter = csv.writer(keyfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
