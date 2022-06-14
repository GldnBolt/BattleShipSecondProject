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
font_dfcltd = font.Font(family = "8BIT WONDER", size = 20)
font_register = font.Font(family = "8BIT WONDER", size = 20)
font_entry = font.Font(family = "8BIT WONDER", size = 15)
font_user = font.Font(family = "8BIT WONDER", size = 15)
font_cnt = font.Font(family = "8BIT WONDER", size = 10)
font_play = font.Font(family = "8BIT WONDER", size = 25)

#Creacion de los canvas
Inicio_c = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray")
About_c = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray" )
Dificultad_c = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray" )
Puntajes_c = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray")
Juego_c = tk.Canvas(window, width = 1500, height = 1000, bg = "Gray")

#Imagenes
###################################################

#Imagen de About
About_Image = tk.PhotoImage(file = "Bar.png")
About_c.create_image(750, 500, image = About_Image)

#Fondo de la ventana
Bg = tk.PhotoImage(file = "WarShip.png")
Inicio_c.create_image(750, 500, image = Bg)

#Logo de la ventana
Logo = tk.PhotoImage(file = "WarShip_logo.png")
Inicio_c.create_image(750, 300, image = Logo)

#Imagenes de los barcos
Ship_1 = tk.PhotoImage(file = "Ship_1.png")
Ship_2 = tk.PhotoImage(file = "Ship_2.png")
Ship_3 = tk.PhotoImage(file = "Ship_3.png")
Ship_4 = tk.PhotoImage(file = "Ship_4.png")
Ship_5 = tk.PhotoImage(file = "Ship_5.png")
###################################################

Inicio_c.place(x=0, y=0)

#Entrada de Usuario
User_entry = tk.Entry(Inicio_c, justify=tk.LEFT,width = 10,font = font_entry, bd = 3)
User_entry.place(x=400, y=600, anchor = "center")

#Entrada de Contraseña
password_entry = tk.Entry(Inicio_c, justify=tk.LEFT, show = "*", width = 10, font = font_entry, bd = 3)
password_entry.place(x=1100, y=600, anchor = "center")

##########################################################################################

#Iniciar Pygame


#Funciones

def about_screen():
    Inicio_c.place_forget()
    Register.place_forget()
    Boton_Puntajes.place_forget()
    Boton_About.place_forget()
    Boton_Exit.place_forget()
    About_c.place(x=0,y=0)
    About_c.focus_force()

    def back():
        About_c.place_forget()
        Inicio_c.place(x=0, y=0)
        Dificultad.place(x = 750, y = 800, anchor = "center")
        Boton_Puntajes.place(x=1500, y=1000, anchor = "se")
        Boton_About.place(x=1500, y=0, anchor = "ne")
        Boton_Exit.place(x=0, y=0, anchor = "nw")

    btn_back = tk.Button(About_c, text = "Back", width=5, height=2, font = font_user, command = back)
    btn_back.place(x=1500,y=0, anchor = "ne")


def dif_screen():
    Inicio_c.place_forget()
    Register.place_forget()
    Boton_Puntajes.place_forget()
    Boton_About.place_forget()
    Boton_Exit.place_forget()
    Dificultad_c.place(x=0,y=0)
    Dificultad_c.focus_force()

    #Barco 1x1
    Dificultad_c.create_image(600, 150, image = Ship_1)

    OPTIONS = [1,2,3,4]
    variable = tk.IntVar(Dificultad_c)
    variable.set("Cantidad de Barcos Tipo 1")
    Ship_1_menu = tk.OptionMenu(Dificultad_c, variable, *OPTIONS)
    Ship_1_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    Ship_1_menu.place(x=900,y=150, anchor = "center")

    #Barco 1x2
    Dificultad_c.create_image(600, 250, image = Ship_2)

    OPTIONS = [1,2,3,4]
    variable = tk.IntVar(Dificultad_c)
    variable.set("Cantidad de Barcos Tipo 2")
    Ship_2_menu = tk.OptionMenu(Dificultad_c, variable, *OPTIONS)
    Ship_2_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    Ship_2_menu.place(x=900,y=250, anchor = "center")

    #Barco 1x3
    Dificultad_c.create_image(600, 350, image = Ship_3)

    OPTIONS = [1,2,3,4]
    variable = tk.IntVar(Dificultad_c)
    variable.set("Cantidad de Barcos Tipo 3")
    Ship_3_menu = tk.OptionMenu(Dificultad_c, variable, *OPTIONS)
    Ship_3_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    Ship_3_menu.place(x=900,y=350, anchor = "center")

    #Barco 1x4
    Dificultad_c.create_image(600, 450, image = Ship_4)

    OPTIONS = [1,2,3,4]
    variable = tk.IntVar(Dificultad_c)
    variable.set("Cantidad de Barcos Tipo 4")
    Ship_4_menu = tk.OptionMenu(Dificultad_c, variable, *OPTIONS)
    Ship_4_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    Ship_4_menu.place(x=900,y=450, anchor = "center")

    #Barco 1x5
    Dificultad_c.create_image(600, 550, image = Ship_5)

    OPTIONS = [1,2,3,4]
    variable = tk.IntVar(Dificultad_c)
    variable.set("Cantidad de Barcos Tipo 5")
    Ship_5_menu = tk.OptionMenu(Dificultad_c, variable, *OPTIONS)
    Ship_5_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    Ship_5_menu.place(x=900,y=550, anchor = "center")

    

    def back():
        Dificultad_c.place_forget()
        Inicio_c.place(x=0, y=0)
        Dificultad.place(x = 750, y = 800, anchor = "center")
        Boton_Puntajes.place(x=1500, y=1000, anchor = "se")
        Boton_About.place(x=1500, y=0, anchor = "ne")
        Boton_Exit.place(x=0, y=0, anchor = "nw")

    btn_back = tk.Button(Dificultad_c, text = "Back", width=5, height=2, font = font_user, command = back)
    btn_back.place(x=1500,y=0, anchor = "ne")

    Play = tk.Button(Dificultad_c, text = "Play", font = font_play, width = 15, height = 2, activebackground = "white", bg = "gray", fg = "white", command = dif_screen)
    Play.place(x = 750, y = 800, anchor = "center")       

def Exit():
    window.destroy()
##########################################################################################

#Botones
Dificultad = tk.Button(Inicio_c, text = "Elegir Dificultad", font = font_dfcltd, width = 15, height = 2, activebackground = "white", bg = "gray", fg = "white", command = dif_screen)
Dificultad.place(x = 950, y = 800, anchor = "center")

Register = tk.Button(Inicio_c, text = "Register", font = font_register, width = 10, height = 2, activebackground = "white", bg = "gray", fg = "white")
Register.place(x = 550, y = 800, anchor = "center")

Boton_Puntajes = tk.Button(Inicio_c, text = "PUNTAJES", font=('Courier', 18, 'bold'))
Boton_Puntajes.place(x=1500, y=1000, anchor = "se")

Boton_About = tk.Button(Inicio_c, text = "ABOUT", font=('Courier', 18, 'bold'), command = about_screen)
Boton_About.place(x=1500, y=0, anchor = "ne")

Boton_Exit = tk.Button(Inicio_c, text = "Exit", font=('Courier', 18, 'bold'), command = Exit)
Boton_Exit.place(x=0, y=0, anchor = "nw")






window.mainloop()



