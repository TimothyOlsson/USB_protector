import shutil
import os
directory=r'C:/TOTALLYNOTHINGSUSPICIOUS'
cwd=directory

shutil.make_archive(cwd+'/'+'data', 'zip', cwd+'/'+'data')

filelist = [f for f in os.listdir(cwd+'/'+'data')]
for f in filelist:
    try:
        os.remove(cwd+'/'+'data'+'/'+f)
    except:
        pass
