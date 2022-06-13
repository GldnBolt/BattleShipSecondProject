from msilib.schema import IniFile
import pygame, sys
import tkinter as tk
import math 
import glob
import os
from threading import Thread
from PIL import ImageTk, Image
import time
import tkinter.font as font

"""



    *************************************************************************************
                           
                             Instituto Tecnológico de Costa Rica
                                Ingenieria en Computadores
    Lenguaje: Python Versión 3.10
    Autor: Andres Blanco Coto (2022108841) y Claudio Arce 
    Versión del programa: Visual Studio Code
    Fecha de la última modificación: 7/6/2022
    Proyecto de Programacion: Battleship. 

    *************************************************************************************

"""



window = tk.Tk()  
window.title("WarShip Wars")
window.minsize(width = 1200, height = 800)
window.resizable(False, False)    

fontplay = font.Font(family = "8BIT WONDER", size = 25) 

Inicio = tk.Canvas(window, width = 1200, height = 800, bg = "Gray")
Inicio.pack()


Bg = ImageTk.PhotoImage(file = "WarShip.png")
Inicio.create_image(600, 400, image = Bg)


Logo = ImageTk.PhotoImage(file = "WarShip_logo.png")
Inicio.create_image(600, 300, image = Logo)

Play = tk.Button(window, text = "Play", font = fontplay, width = 10, height = 2, activebackground = "white", bg = "gray", fg = "white")
    
Play.place(x = 600 , y = 600, anchor = "center")





window.mainloop()



