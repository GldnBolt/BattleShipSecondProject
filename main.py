import pygame, sys
import tkinter as tk
import math 
import glob
import os
from threading import Thread
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

#Canvas

Inicio = tk.Canvas(main_window, 
    width = 1200, 
    height = 800, 
    bg = "Gray")


##########################################################################################

#Funciones

##########################################################################################


#Creacion del canvas

Inicio.place(
    x=0,
    y=0)

#Entrada de Usuario
User_entry = tk.Entry(
        justify=tk.LEFT,
        width = 10,
        font = font_entry, 
        bd = 3)
User_entry.place(
        x=200, 
        y=400,
        anchor = "center")

#Entrada de Contraseña
password_entry = tk.Entry(
        justify=tk.LEFT,
        show = "*",
        width = 10,
        font = font_entry, 
        bd = 3)
password_entry.place(
        x=1000, 
        y=400,
        anchor = "center")
#Fondo de los entrys
Fondo_entry = tk.Label(
        Inicio, 
        width=50, 
        height=15, 
        bg="dimgray")
Fondo_entry.place(
        x=600,
        y=550,
        anchor = "center")

#Fondo de la ventana
Bg = tk.PhotoImage(file = "WarShip.png")
Inicio.create_image(
    600, 
    400, 
    image = Bg)

#Logo de la ventana
Logo = tk.PhotoImage(file = "WarShip_logo.png")
Inicio.create_image(
    600, 
    300, 
    image = Logo)

#Boton
Play = tk.Button(
    Inicio, 
    text = "Play", 
    font = fontplay, 
    width = 10, 
    height = 2, 
    activebackground = "white", 
    bg = "gray", 
    fg = "white")
Play.place(
    x = 600, 
    y = 600,
    anchor = "center")



main_window.mainloop()



