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

#Importar ventanas
import user_screen

"""



    *************************************************************************************
                           
                             Instituto Tecnológico de Costa Rica
                                Ingenieria en Computadores
    Lenguaje: Python Versión 3.10
    Autor: Andres Blanco Coto (2022108841) y Claudio Arce (201058559)
    Versión del programa: Visual Studio Code
    Fecha de la última modificación: 7/6/2022
    Proyecto de Programacion: Battleship. 

    *************************************************************************************

"""


#Ventana
main_window = tk.Tk()  
main_window.title("WarShip Wars")
main_window.minsize(width = 1200, height = 800)
main_window.resizable(False, False)    

#Fuente de texto
fontplay = font.Font(family = "8BIT WONDER", size = 25)
font_entry = font.Font(family = "8BIT WONDER", size = 15)
font_user = font.Font(family = "8BIT WONDER", size = 10)

##########################################################################################

#Funciones

def user_screen():
    main_window.iconify()
    main_window.withdraw(user_screen)
    




##########################################################################################

#Creacion del canvas
Inicio = tk.Canvas(
    main_window, 
    width = 1200, 
    height = 800, 
    bg = "Gray")
Inicio.pack()


#Fondo de la ventana
Bg = ImageTk.PhotoImage(file = "WarShip.png")
Inicio.create_image(
    600, 
    400, 
    image = Bg)

#Logo de la ventana
Logo = ImageTk.PhotoImage(file = "WarShip_logo.png")
Inicio.create_image(
    600, 
    300, 
    image = Logo)

#Boton
Play = tk.Button(
    main_window, 
    text = "Play", 
    font = fontplay, 
    width = 10, 
    height = 2, 
    activebackground = "white", 
    bg = "gray", 
    fg = "white", 
    command = user_screen)
Play.place(
    x = 600, 
    y = 600,
    anchor = "center")







main_window.mainloop()



