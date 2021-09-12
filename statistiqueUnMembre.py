import matplotlib.pyplot as plt
from tkinter import*
import tkinter as tk
from maBibiliotheque import*


nomDeLaPhoto = "stat1.png"

def statistique():
        def goBack():
                fenetre.destroy()
        def a1():
                img = PhotoImage(file="stat1.png")
                canf1 = Canvas(p2, bg = 'blue', width = 500, height = 475)
                canf1.create_image(-80,0,anchor = tk.NW, image = img)
                canf1.image = img
                canf1.grid(column = 2,row= 1)
                
        def a2():
                img = PhotoImage(file="stat2.png")
                canf1 = Canvas(p2, bg = 'blue', width = 500, height = 475)
                canf1.create_image(-80,0,anchor = tk.NW, image = img)
                canf1.image = img
                canf1.grid(column = 2,row= 1)
        def a3():
                nomDeLaPhoto = "stat3.png"
                img = PhotoImage(file=nomDeLaPhoto)
                canf1 = Canvas(p2, bg = 'blue', width = 500, height = 475)
                canf1.create_image(-80,0,anchor = tk.NW, image = img)
                canf1.image = img
                canf1.grid(column = 2,row= 1)

        graph()
        
        fenetre = Toplevel()
        fenetre.geometry("500x580+500+200")
        fenetre.title("stat")

        p1=PanedWindow(fenetre)
        p1.grid(row=0, column=0)
        p2=PanedWindow(fenetre)
        p2.grid(row=1, column=0)
        p3=PanedWindow(fenetre)
        p3.grid(row=2, column=0)

        button1 = Button(p1, text = "Homme Femme",width=23, command = a1)
        button1.grid(row = 1, column = 1)
        button2 = Button(p1, text = "Cours suivit",width=23, command = a2)
        button2.grid(row = 1, column = 2)
        button3 = Button(p1, text = "Pourcentage Aéro",width=23, command = a3 )
        button3.grid(row = 1, column = 3)

        img = PhotoImage(file=nomDeLaPhoto)
        canf1 = Canvas(p2, bg = 'blue', width = 500, height = 475)
        canf1.create_image(-80,0,anchor = tk.NW, image = img)
        canf1.image = img
        canf1.grid(column = 2,row= 1)

        button4 = Button(p3, text = "Retour",width=23, command = goBack )
        button4.grid(row = 0, column = 0)
