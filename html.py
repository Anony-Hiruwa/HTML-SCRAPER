import requests
import sys,time,os
import urllib.request

class c:
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    red = '\033[31m'
    pink = '\033[35m'
    yellow = '\033[33m'
    
def print1(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 200)
        
def print2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 10)


banner = c.cyan + """

       /$$   /$$ /$$$$$$$$ /$$      /$$ /$$      
       | $$  | $$|__  $$__/| $$$    /$$$| $$      
       | $$  | $$   | $$   | $$$$  /$$$$| $$      
       | $$$$$$$$   | $$   | $$ $$/$$ $$| $$      
       | $$__  $$   | $$   | $$  $$$| $$| $$      
       | $$  | $$   | $$   | $$\  $ | $$| $$      
       | $$  | $$   | $$   | $$ \/  | $$| $$$$$$$$
       |__/  |__/   |__/   |__/     |__/|________/
       
       
                  """+c.blue+"""<< TOOL BY HIRUWA >>
                  
                 """+c.green+"""--> HTML SCRAPPER <--
""" 

print1(banner.center(50))

########REQUEST######
print2(c.cyan+"NOW GIVE ME WEBSITE LINK FOR GET HTML CODES ......\n\n")
web = input(c.cyan+"Enter Your website Link : ".center(20))
url = web
x = requests.post(url)

#######Get Details########
os.system("clear")
out = x.text
print(c.yellow+x.text)



print2(c.cyan+"YOU WANT TO SAVE THIS HTML CODE TO YOUR PHONE")
save = input("Enter Y to save , N to Rerun this tool , E to Exit this tool\n\n[Y] SAVE\n[N] RERUN\n[E] EXIT \n------> ")

if save == "Y":
    f = open("/storage/emulated/0/HTML/Trex-Html.html", "w")
    f.write(out)
    f.close()
    
if save == 'N':
    os.system('clear')
    os.system('python html.py')
   
if save  == 'E':
        os.system('exit')

else :
    print2("WRONG CHOICE AUTOMATICALLY RERUN.......")
    os.system('python html.py')

