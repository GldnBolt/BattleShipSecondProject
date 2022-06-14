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
    Fecha de la última modificación: 14/6/2022
    Proyecto de Programacion: WarShip Wars

    *************************************************************************************

"""


#Ventana
main_window = tk.Tk()  
main_window.title("WarShip Wars")
main_window.minsize(width = 1500, height = 1000)
main_window.resizable(False, False)    

##########################################################################################

#Funciones

##########################################################################################

#Fuente de texto
fontplay = font.Font(family = "8BIT WONDER", size = 25)
font_entry = font.Font(family = "8BIT WONDER", size = 15)
font_user = font.Font(family = "8BIT WONDER", size = 10)

#Creacion de los canvas
Inicio = tk.Canvas(main_window, width = 1500, height = 1000, bg = "Gray")
About = tk.Canvas(main_window, width = 1500, height = 1000, bg = "Gray" )
Juego = tk.Canvas(main_window, width = 1500, height = 1000, bg = "Gray" )
Puntajes = tk.Canvas(main_window, width = 1500, height = 1000, bg = "Gray")

#Fondo de la ventana
Bg = tk.PhotoImage(file = "WarShip.png")
Inicio.create_image(750, 500, image = Bg)

#Logo de la ventana
Logo = tk.PhotoImage(file = "WarShip_logo.png")
Inicio.create_image(750, 300, image = Logo)

Inicio.place(x=0, y=0)

#Entrada de Usuario
User_entry = tk.Entry(justify=tk.LEFT,width = 10,font = font_entry, bd = 3)
User_entry.place(x=200, y=400, anchor = "center")

#Entrada de Contraseña
password_entry = tk.Entry(justify=tk.LEFT, show = "*", width = 10, font = font_entry, bd = 3)
password_entry.place(x=1000, y=400, anchor = "center")

#Botones
Play = tk.Button(Inicio, text = "Play", font = fontplay, width = 10, height = 2, activebackground = "white", bg = "gray", fg = "white")
Play.place(x = 750, y = 700, anchor = "center")

Boton_Puntajes = tk.Button(Inicio, text="PUNTAJES", font=('Courier', 18, 'bold'), command=test)
Boton_Puntajes.place(x=500, y=640)

Boton_About = tk.Button(Inicio, text="ABOUT", font=('Courier', 18, 'bold'), command=test)
Boton_About.place(x=800, y=640)

Boton_Salir = tk.Button(Inicio, text="Salir", font=('Courier', 18, 'bold'), command=test)
Boton_Salir.place(x=1000, y=640)





main_window.mainloop()



