#CODED BY HIRUWA


import os
import time

print('INSTALLING DEPENDENCIES.....')
print('wait.....')
time.sleep(2)
path = "/storage/emulated/0/"
os.chdir(path)
nfol = "HTML"
os.makedirs(nfol)
os.system('clear')
print('SUCCESFULLY INSTALLED')
time.sleep(2)
os.system('clear')
print('AUTOMATICALLY START HTML SCRAPER TOOL.....')
os.system('clear')
os.system('python html.py')
