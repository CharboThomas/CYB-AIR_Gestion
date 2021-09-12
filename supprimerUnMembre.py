from maBibiliotheque import* ### on importe la fonction supress
from tkinter import*
import tkinter as tk
    
def delate():
    def priseValeur():
        information1 = entre1.get()
        information2 = entre2.get()
        supress(information1,information2)
        label3 = Label(fenetreDel, text = "Personne supprimer de notre fichier")
        label3.grid(row = 3, column = 1)
    def back():
        fenetreDel.destroy()

    fenetreDel = tk.Tk()
    fenetreDel.geometry("450x250+500+200")
    fenetreDel.title("Suprimer un membre")

    label0 = Label(fenetreDel, text = "Vueillez entrer le nom et le prénom de la personne visée")
    label0.grid(row = 0, column = 1)

    label1 = Label(fenetreDel, text = "Nom:")
    label1.grid(row = 1, column = 0)
    label2 = Label(fenetreDel, text = "Prénom:")
    label2.grid(row = 2, column = 0)

    entre1 = Entry(fenetreDel)
    entre1.grid(row = 1, column = 1)
    entre2 = Entry(fenetreDel)
    entre2.grid(row = 2, column = 1)

    entre1 = Entry(fenetreDel)
    entre1.grid(row = 1, column = 1)

    button1 = Button(fenetreDel, text="Retour", command = back)
    button1.grid(row = 10, column = 0)
    button2 = Button(fenetreDel, text="Suprimer",command = priseValeur)
    button2.grid(row = 10, column = 2)

