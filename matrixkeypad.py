import RPi.GPIO as GPIO
import Keypad   #import module Keypad
import os

ROWS = 4       # number of rows of the Keypad
COLS = 4       #number of columns of the Keypad

keys = [ '1','2','3','A',         #key code
         '4','5','6','B',
         '7','8','9','C',
         '*','0','#','D'     ]

rowsPins = [12,16,18,22]       #connect to the row pinouts of the keypad
colsPins = [19,15,13,11]       #connect to the column pinouts of the keypad

print("Welcome to your new home lock system")
print("Please Enter User Password: ")

def check_pressed_keys():
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
    keypad.setDebounceTime(50)      #set the debounce time
    result = ""
    while(True):
        key = keypad.getKey()       #obtain the state of keys
        if(key != keypad.NULL):     #if there is key pressed, print its key code.
            result = result + key
            #print("You Pressed Key : %c "%(key))
            if len(result) == len(password):
                return result
            #print(result)     # This is just to allow you see what keys are pressed


password = "A1234"
result = check_pressed_keys()

try:
    if result == password:
        print("Unlocked! Enjoy! ")
        print("Access Granted!")

    else:
        print("Alert! Wrong password, try again")   

except KeyboardInterrupt:      #When 'Ctrl+C' is pressed, exit the program.
        GPIO.cleanup()
        





