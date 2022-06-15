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
font_entry = font.Font(family = "8BIT WONDER", size = 20)
font_user = font.Font(family = "8BIT WONDER", size = 15)
font_cnt = font.Font(family = "8BIT WONDER", size = 10)
font_play = font.Font(family = "8BIT WONDER", size = 25)

#Creacion de los canvas
Inicio_C = tk.Canvas(window, width = 1500, height = 1000, bg ="Gray")
About_C = tk.Canvas(window, width = 1500, height = 1000, bg ="Gray")
Dificultad_C = tk.Canvas(window, width = 1500, height = 1000, bg ="Gray")
Puntajes_C = tk.Canvas(window, width = 1500, height = 1000, bg ="Gray")
Juego_C = tk.Canvas(window, width = 1500, height = 1000, bg ="Gray")
Registro_C = tk.Canvas(window, width = 1500, height = 1000, bg ="Gray")

#Imagenes
###################################################

#Imagen de registro
Reg_image = tk.PhotoImage(file = "Images\Bg\Register_bg.png")

#Imagen de About
About_Image = tk.PhotoImage(file = "Images\Bar.png")
About_C.create_image(750, 500, image = About_Image)

#Fondo de la ventana
Bg = tk.PhotoImage(file = "Images\Bg\WarShip.png")
Inicio_C.create_image(750, 500, image = Bg)

#Logo de la ventana
Logo = tk.PhotoImage(file = "Images\WarShip_logo.png")
Inicio_C.create_image(750, 300, image = Logo)

#Imagenes de los barcos
#Ship_1 = tk.PhotoImage(file = "C:\Users\Xpc\Documents\GitHub\BattleShipSecondProject\Images\Ships\Ship_1.png")
Ship_2 = tk.PhotoImage(file = "Images\Ships\Ship_2.png")
Ship_3 = tk.PhotoImage(file = "Images\Ships\Ship_3.png")
Ship_4 = tk.PhotoImage(file = "Images\Ships\Ship_4.png")
#Ship_5 = tk.PhotoImage(file = "Ship_5.png")
###################################################

Inicio_C.place(x=0, y=0)

#Entrada de Usuario
User_entry = tk.Entry(Inicio_C, justify=tk.LEFT, width = 10, font = font_entry, bd = 3)
User_entry.place(x=550, y=600, anchor = "center")

#Entrada de Contraseña
password_entry = tk.Entry(Inicio_C, justify=tk.LEFT, show ="*", width = 12, font = font_entry, bd = 3)
password_entry.place(x=950, y=600, anchor = "center")

##########################################################################################

#Iniciar Pygame


#Funciones

def about_screen():
    Inicio_C.place_forget()
    Register.place_forget()
    Boton_Puntajes.place_forget()
    Boton_About.place_forget()
    Boton_Exit.place_forget()
    About_C.place(x=0, y=0)
    About_C.focus_force()

    def back():
        About_C.place_forget()
        Inicio_C.place(x=0, y=0)
        Log_In.place(x = 550, y = 800, anchor = "center")
        Register.place(x=950, y=800, anchor="center")
        Boton_Puntajes.place(x=1500, y=1000, anchor = "se")
        Boton_About.place(x=1500, y=0, anchor = "ne")
        Boton_Exit.place(x=0, y=0, anchor = "nw")

    btn_back = tk.Button(About_C, text ="Back", width=5, height=2, font = font_user, command = back)
    btn_back.place(x=1500,y=0, anchor = "ne")

def reg_screen():
    Inicio_C.place_forget()
    Register.place_forget()
    Boton_Puntajes.place_forget()
    Boton_About.place_forget()
    Boton_Exit.place_forget()
    Registro_C.place(x=0, y=0)
    Registro_C.focus_force()

    Registro_C.create_image(750,500, image = Reg_image)

    Name_E = tk.Entry(Registro_C, justify=tk.LEFT, width=10, font=font_entry, bd=3)
    Name_E.place(x=750, y=250, anchor="center")
    L_Name_E = tk.Entry(Registro_C, justify=tk.LEFT, width=10, font=font_entry, bd=3)
    L_Name_E.place(x=750, y=450, anchor="center")
    User_E = tk.Entry(Registro_C, justify=tk.LEFT, width=10, font=font_entry, bd=3)
    User_E.place(x=750, y=650, anchor="center")
    Password_E = tk.Entry(Registro_C, justify=tk.LEFT, width=10, font=font_entry, bd=3)
    Password_E.place(x=750, y=850, anchor="center")

    def back():
        Registro_C.place_forget()
        Inicio_C.place(x=0, y=0)
        Log_In.place(x = 550, y = 800, anchor = "center")
        Register.place(x=950, y=800, anchor="center")
        Boton_Puntajes.place(x=1500, y=1000, anchor = "se")
        Boton_About.place(x=1500, y=0, anchor = "ne")
        Boton_Exit.place(x=0, y=0, anchor = "nw")

    btn_back = tk.Button(Registro_C, text ="Back", width=5, height=2, font = font_user, command = back)
    btn_back.place(x=1500,y=0, anchor = "ne")


def dif_screen():
    Inicio_C.place_forget()
    Register.place_forget()
    Boton_Puntajes.place_forget()
    Boton_About.place_forget()
    Boton_Exit.place_forget()
    Dificultad_C.place(x=0, y=0)
    Dificultad_C.focus_force()

    # #Barco 1x1
    # Dificultad_c.create_image(600, 150, image = Ship_1)
    #
    # OPTIONS = [1,2,3,4]
    # variable = tk.IntVar(Dificultad_c)
    # variable.set("Cantidad de Barcos Tipo 1")
    # Ship_1_menu = tk.OptionMenu(Dificultad_c, variable, *OPTIONS)
    # Ship_1_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    # Ship_1_menu.place(x=900,y=150, anchor = "center")

    #Barco 1x2
    Dificultad_C.create_image(600, 250, image = Ship_2)

    OPTIONS = [1,2,3,4]
    variable = tk.IntVar(Dificultad_C)
    variable.set("Cantidad de Barcos Tipo 2")
    Ship_2_menu = tk.OptionMenu(Dificultad_C, variable, *OPTIONS)
    Ship_2_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    Ship_2_menu.place(x=900,y=250, anchor = "center")

    #Barco 1x3
    Dificultad_C.create_image(600, 350, image = Ship_3)

    OPTIONS = [1,2,3,4]
    variable = tk.IntVar(Dificultad_C)
    variable.set("Cantidad de Barcos Tipo 3")
    Ship_3_menu = tk.OptionMenu(Dificultad_C, variable, *OPTIONS)
    Ship_3_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    Ship_3_menu.place(x=900,y=350, anchor = "center")

    #Barco 1x4
    Dificultad_C.create_image(600, 450, image = Ship_4)

    OPTIONS = [1,2,3,4]
    variable = tk.IntVar(Dificultad_C)
    variable.set("Cantidad de Barcos Tipo 4")
    Ship_4_menu = tk.OptionMenu(Dificultad_C, variable, *OPTIONS)
    Ship_4_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    Ship_4_menu.place(x=900,y=450, anchor = "center")

    #Barco 1x5
    #Dificultad_c.create_image(600, 550, image = Ship_5)

    # OPTIONS = [1,2,3,4]
    # variable = tk.IntVar(Dificultad_c)
    # variable.set("Cantidad de Barcos Tipo 5")
    # Ship_5_menu = tk.OptionMenu(Dificultad_c, variable, *OPTIONS)
    # Ship_5_menu.config(width=25, height=2, activebackground="dimgray", bg = "white", font = font_cnt)
    # Ship_5_menu.place(x=900,y=550, anchor = "center")

    def back():
        Dificultad_C.place_forget()
        Inicio_C.place(x=0, y=0)
        Log_In.place(x = 550, y = 800, anchor = "center")
        Register.place(x=950, y=800, anchor="center")
        Boton_Puntajes.place(x=1500, y=1000, anchor = "se")
        Boton_About.place(x=1500, y=0, anchor = "ne")
        Boton_Exit.place(x=0, y=0, anchor = "nw")

    btn_back = tk.Button(Dificultad_C, text ="Back", width=5, height=2, font = font_user, command = back)
    btn_back.place(x=1500,y=0, anchor = "ne")


    Play.place(x=750, y=800, anchor="center")

def play_screen():
    Dificultad_C.place_forget()
    Juego_C.place(x=0, y=0)

    def back():
        Juego_C.place_forget()
        dif_screen()

    btn_back = tk.Button(Juego_C, text="Back", width=5, height=2, font=font_user, command=back)
    btn_back.place(x=1500, y=0, anchor="ne")




def Exit():
    window.destroy()
##########################################################################################

#Botones
Log_In = tk.Button(Inicio_C, text ="Log In", font = font_dfcltd, width = 10, height = 2, activebackground ="white", bg ="gray", fg ="white", command = dif_screen)
Log_In.place(x = 550, y = 800, anchor = "center")

Register = tk.Button(Inicio_C, text ="Register", font = font_register, width = 10, height = 2, activebackground ="white", bg ="gray", fg ="white", command=reg_screen)
Register.place(x = 950, y = 800, anchor = "center")

Boton_Puntajes = tk.Button(Inicio_C, text ="PUNTAJES", font=('Courier', 18, 'bold'))
Boton_Puntajes.place(x=1500, y=1000, anchor = "se")

Boton_About = tk.Button(Inicio_C, text ="ABOUT", font=('Courier', 18, 'bold'), command = about_screen)
Boton_About.place(x=1500, y=0, anchor = "ne")

Boton_Exit = tk.Button(Inicio_C, text ="Exit", font=('Courier', 18, 'bold'), command = Exit)
Boton_Exit.place(x=0, y=0, anchor = "nw")

Play = tk.Button(Dificultad_C, text="Play", font=font_play, width=15, height=2, activebackground="white", bg ="gray", fg="white", command=play_screen)


window.mainloop()



