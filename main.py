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
window = tk.Tk()  
window.title("WarShip Wars")
window.minsize(width = 1500, height = 1000)
window.resizable(False, False)    

#Fuente de texto
font_play = font.Font(family = "8BIT WONDER", size = 25)
font_register = font.Font(family = "8BIT WONDER", size = 15)
font_entry = font.Font(family = "8BIT WONDER", size = 15)
font_user = font.Font(family = "8BIT WONDER", size = 10)

#Creacion de los canvas
Inicio = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray")
About = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray" )
Juego = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray" )
Puntajes = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray")

#Fondo de la ventana
Bg = tk.PhotoImage(file = "WarShip.png")
Inicio.create_image(750, 500, image = Bg)

#Logo de la ventana
Logo = tk.PhotoImage(file = "WarShip_logo.png")
Inicio.create_image(750, 300, image = Logo)

Inicio.place(x=0, y=0)

#Entrada de Usuario
User_entry = tk.Entry(Inicio, justify=tk.LEFT,width = 10,font = font_entry, bd = 3)
User_entry.place(x=400, y=600, anchor = "center")

#Entrada de Contraseña
password_entry = tk.Entry(Inicio, justify=tk.LEFT, show = "*", width = 10, font = font_entry, bd = 3)
password_entry.place(x=1100, y=600, anchor = "center")

##########################################################################################

#Funciones

def about_screen():

    Inicio.place_forget()

    Register.place_forget()
    Boton_Puntajes.place_forget()
    Boton_About.place_forget()
    Boton_Exit.place_forget()

    About.place(x=0,y=0)

    def back():
        About.place_forget()
        Inicio.place(x=0, y=0)
        Play.place(x = 750, y = 800, anchor = "center")
        Boton_Puntajes.place(x=1500, y=1000, anchor = "se")
        Boton_About.place(x=1500, y=0, anchor = "ne")
        Boton_Exit.place(x=0, y=0, anchor = "nw")

    btn_back = tk.Button(About, text = "Back", font = font_user, command = back)
    btn_back.place(x=1500,y=0, anchor = "ne")

def Exit():
    window.destroy()

##########################################################################################

#Botones
Play = tk.Button(Inicio, text = "Play", font = font_play, width = 10, height = 2, activebackground = "white", bg = "gray", fg = "white")
Play.place(x = 750, y = 800, anchor = "center")

Register = tk.Button(Inicio, text = "Register", font = font_register, width = 10, height = 2, activebackground = "white", bg = "gray", fg = "white")
Register.place(x = 500, y = 500, anchor = "center")

Boton_Puntajes = tk.Button(Inicio, text = "PUNTAJES", font=('Courier', 18, 'bold'))
Boton_Puntajes.place(x=1500, y=1000, anchor = "se")

Boton_About = tk.Button(Inicio, text = "ABOUT", font=('Courier', 18, 'bold'), command = about_screen)
Boton_About.place(x=1500, y=0, anchor = "ne")

Boton_Exit = tk.Button(Inicio, text = "Exit", font=('Courier', 18, 'bold'), command = Exit)
Boton_Exit.place(x=0, y=0, anchor = "nw")






window.mainloop()



