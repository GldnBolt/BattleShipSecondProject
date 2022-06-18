import pyfirmata
from pyfirmata import Arduino, util
import time
import random
import keyboard
import tkinter as tk
arduino = Arduino('COM4')


window = tk.Tk()  
window.title("Arduino test")
window.minsize(width = 1500, height = 1000)
window.resizable(False, False) 

test_c = tk.Canvas(window, width = 1500, height = 1000, bg ="Gray")
test_c.place(x=750,y=500,anchor="center")

X_POS = 100
Y_POS = 100

pinUP = arduino.get_pin('d:8:i')
pinDOWN = arduino.get_pin('d:9:i')
pinLEFT = arduino.get_pin('d:10:i')
pinRIGHT = arduino.get_pin('d:11:i')
pinPLACE = arduino.get_pin('d:12:i')

d = pinRIGHT.read() #Se leen los pines del arduino 
s = pinDOWN.read()
a = pinLEFT.read()
w = pinUP.read()
e = pinPLACE.read()

rect = tk.Label(test_c, width=5, height=5, bg = "red")
rect.place(x=X_POS, y= Y_POS)

def mov_push_btn():

    if w == True:
        Y_POS += 10
    elif s == True:
        Y_POS -= 10

    elif a == True:
        X_POS -= 10
    elif d == True:
        Y_POS += 10

    elif e == True:
        rect.config(bg = "blue")


window.mainloop()
    
                                    