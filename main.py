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
def open_play_screen():
    pass
    
def open_user_screen():
    
    main_window.iconify()

    User_screen = tk.Toplevel()
    User_screen.minsize(
        width = 1200, 
        height = 800)        
    User_screen.title("Pantalla de Usuario")
    User_screen.resizable(False,False)

    #Label de entrada de Usuario
    Fondo_entry = tk.Label(
        User_screen, 
        width=50, 
        height=15, 
        bg="dimgray")
    Fondo_entry.place(
        x=600,
        y=550,
        anchor = "center")

    #Entrada de Usuario
    User_entry = tk.Entry(
        justify=tk.LEFT,
        width = 10,
        font = font_entry, 
        bd = 3)
    User_entry.place(
        x=600, 
        y=500,
        anchor = "center")

    #Entrada de Contraseña
    password_entry = tk.Entry(
        justify=tk.LEFT,
        show = "*",
        width = 10,
        font = font_entry, 
        bd = 3)
    password_entry.place(
        x=600, 
        y=600,
        anchor = "center")

    btn_play = tk.Button(
        User_screen, 
        text = "Play", 
        font = fontplay, 
        width = 10, 
        height = 2, 
        activebackground = "white", 
        bg = "gray", 
        fg = "white", 
        command = open_play_screen)
    btn_play.place(
        x = 600, 
        y = 600,
        anchor = "center")
    
##########################################################################################


#Creacion del canvas
Inicio = tk.Canvas(main_window, 
    width = 1200, 
    height = 800, 
    bg = "Gray")
Inicio.pack()


#Fondo de la ventana
Bg = ImageTk.PhotoImage(file = "WarShip.png")
Inicio.create_image(600, 400, image = Bg)

#Logo de la ventana
Logo = ImageTk.PhotoImage(file = "WarShip_logo.png")
Inicio.create_image(600, 300, image = Logo)

#Boton
Play = tk.Button(
    Inicio, 
    text = "Play", 
    font = fontplay, 
    width = 10, 
    height = 2, 
    activebackground = "white", 
    bg = "gray", 
    fg = "white", 
    command = open_user_screen)
Play.place(
    x = 600, 
    y = 600,
    anchor = "center")

#Creacion ventana de Usuario
"""
    #Creacion del canvas
    Inicio = tk.Canvas(
        user_window, 
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

    #Label de entrada de Usuario
    Fondo_entry = tk.Label(
        user_window, 
        width=50, 
        height=15, 
        bg="dimgray")
    Fondo_entry.place(
        x=600,
        y=550,
        anchor = "center")

    #Entrada de Usuario
    User_entry = tk.Entry(
        justify=tk.LEFT,
        width = 10,
        font = font_entry, 
        bd = 3)
    User_entry.place(
        x=600, 
        y=500,
        anchor = "center")

    #Entrada de Contraseña
    password_entry = tk.Entry(
        justify=tk.LEFT,
        show = "*",
        width = 10,
        font = font_entry, 
        bd = 3)
    password_entry.place(
        x=600, 
        y=600,
        anchor = "center")

    user_window.mainloop()
"""







main_window.mainloop()



