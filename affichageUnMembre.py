from tkinter import *
from maBibiliotheque import*


def show():
    root = Tk()
    root.title("Cyber.affichageDesMembres")

    truc = "normal"
    liste = affichage(truc)

    quote1 = liste[0]
    quote2 = liste[1]
    quote3 = liste[2]
    quote4 = liste[3]
    quote5 = liste[4]
    quote6 = liste[5]
    quote7 = liste[6]
    
    def destroy():
        root.destroy()

    def vider():
        text2.delete(1.0,END)
        text3.delete(1.0,END)
        text4.delete(1.0,END)
        text5.delete(1.0,END)
        text6.delete(1.0,END)
        text7.delete(1.0,END)
        text8.delete(1.0,END)

    def STK():
        vider()
        truc = "STK"
        liste = affichage(truc)
        quote1 = liste[0]
        quote2 = liste[1]
        quote3 = liste[2]
        quote4 = liste[3]
        quote5 = liste[4]
        quote6 = liste[5]
        quote7 = liste[6]
        text2.insert(END, quote1)
        text3.insert(END, quote2, 'color')
        text4.insert(END, quote3, 'color')
        text5.insert(END, quote4, 'color')
        text6.insert(END, quote5, 'color')
        text7.insert(END, quote6, 'color')
        text8.insert(END, quote7, 'color')

    def Katia():
        vider()
        truc = "Katia"
        liste = affichage(truc)
        quote1 = liste[0]
        quote2 = liste[1]
        quote3 = liste[2]
        quote4 = liste[3]
        quote5 = liste[4]
        quote6 = liste[5]
        quote7 = liste[6]
        text2.insert(END, quote1)
        text3.insert(END, quote2, 'color')
        text4.insert(END, quote3, 'color')
        text5.insert(END, quote4, 'color')
        text6.insert(END, quote5, 'color')
        text7.insert(END, quote6, 'color')
        text8.insert(END, quote7, 'color')

    def Photoshop():
        vider()
        truc = "Photochop"
        liste = affichage(truc)
        quote1 = liste[0]
        quote2 = liste[1]
        quote3 = liste[2]
        quote4 = liste[3]
        quote5 = liste[4]
        quote6 = liste[5]
        quote7 = liste[6]
        text2.insert(END, quote1)
        text3.insert(END, quote2, 'color')
        text4.insert(END, quote3, 'color')
        text5.insert(END, quote4, 'color')
        text6.insert(END, quote5, 'color')
        text7.insert(END, quote6, 'color')
        text8.insert(END, quote7, 'color')

    def Latex():
        vider()
        truc = "Latex"
        liste = affichage(truc)
        quote1 = liste[0]
        quote2 = liste[1]
        quote3 = liste[2]
        quote4 = liste[3]
        quote5 = liste[4]
        quote6 = liste[5]
        quote7 = liste[6]
        text2.insert(END, quote1)
        text3.insert(END, quote2, 'color')
        text4.insert(END, quote3, 'color')
        text5.insert(END, quote4, 'color')
        text6.insert(END, quote5, 'color')
        text7.insert(END, quote6, 'color')
        text8.insert(END, quote7, 'color')

    def c():
        vider()
        truc = "c"
        liste = affichage(truc)
        quote1 = liste[0]
        quote2 = liste[1]
        quote3 = liste[2]
        quote4 = liste[3]
        quote5 = liste[4]
        quote6 = liste[5]
        quote7 = liste[6]
        text2.insert(END, quote1)
        text3.insert(END, quote2, 'color')
        text4.insert(END, quote3, 'color')
        text5.insert(END, quote4, 'color')
        text6.insert(END, quote5, 'color')
        text7.insert(END, quote6, 'color')
        text8.insert(END, quote7, 'color')

    text2 = Text(root, height=30, width=20)
    text2.insert(END, quote1,)#on affiche la chaine de caractère dans la partie text2 de l'interface graphique
    text2.grid(row = 1, column = 1)

    text3 = Text(root, height=30, width=20)
    text3.insert(END, quote2, 'color')
    text3.grid(row = 1, column = 2)

    text4 = Text(root, height=30, width=20)
    text4.insert(END, quote3, 'color')
    text4.grid(row = 1, column = 3)

    text5 = Text(root, height=30, width=20)
    text5.insert(END, quote4, 'color')
    text5.grid(row = 1, column = 4)

    text6 = Text(root, height=30, width=30)
    text6.insert(END, quote5, 'color')
    text6.grid(row = 1, column = 5)

    text7 = Text(root, height=30, width=20)
    text7.insert(END, quote6, 'color')
    text7.grid(row = 1, column = 6)

    text8 = Text(root, height=30, width=30)
    text8.insert(END, quote7, 'color')
    text8.grid(row = 1, column = 7)

    button1 = Button(root,text = "STK",width=22, command =STK)
    button1.grid(row = 2, column = 2)

    button2 = Button(root,text = "Photoshop",width=22,command = Photoshop)
    button2.grid(row = 2, column = 3)

    button3 = Button(root,text = "C++",width=22,command = c)
    button3.grid(row = 2, column = 4)

    button4 = Button(root,text = "Catia",width=34,command = Katia)
    button4.grid(row = 2, column = 5)

    button5 = Button(root,text = "Latex",width=22, command = latex)
    button5.grid(row = 2, column = 6)

    button6 = Button(root,text = "Retour",width=22,command = destroy)
    button6.grid(row = 2, column = 1)

    button7 = Button(root,text = "Vider",width=22,command = vider)
    button7.grid(row = 2, column = 7)

    root.mainloop()
