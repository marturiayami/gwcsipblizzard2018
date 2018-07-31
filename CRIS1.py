#  ~   Command Receptive Interactive Software .Py   ~  #
import pyautogui
import speech_recognition

key_words = ['Location', 'Click', 'Scroll', 'Move to:', 'Close Tab', 'Minimize', 'Full Screen', 'New Window', 'Next Tab', 'New Tab', 'Full Screen', 'Key Words']

print('''Hello and welcome to CRIS.Py. Your personal Command Recognizing Interactive Software! This program will allow you to manuver your personal computer hands free! With specified key words you can manuver over screens, click buttons, open tabs and much more!''')
print("The key words are vocal commands you can say to cause an action. CRIS.Py's key words are as follows: {}".format(key_words))
print("""The 'Move to:' key word functions to allow you to move your mouse anywhere one your screen based on an coordinate. For example if you say 'Move to: 0, 1079' the mouse will move to the bottom left corner of the window.""")
print("To access the key terms just say 'Key Words'. Hope you enjoy!" )

#   ~    HOTKEYS    ~
# ctrl + n = new window   ctrl + tab = next tab
# ctrl + t = new tab      ctrl + F4 = close tab     F11 = full screen
