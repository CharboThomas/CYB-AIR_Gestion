from tkinter import*
from inscription import*
from affichageUnMembre import*
from rechercheUnMembre import*
from supprimerUnMembre import*
from statistiqueUnMembre import*

def destroy():
    fenetre.destroy()

fenetre = Tk()
fenetre.geometry("850x800+0+0")
fenetre.title("Cyber")

background_image=PhotoImage(file="cyber.gif")
background_label = Label(fenetre, image=background_image)
background_label.place(x=0, y=-11, relwidth=1, relheight=1)

button1 = Button(fenetre, text = "Inscription", command = register,width=50 )
button1.place( x=275, y = 300)
button2 = Button(fenetre, text = "Affichage des inscris", command = show,width=50 )
button2.place( x=275, y = 350)
button3 = Button(fenetre, text = "Supprimer un membre", command = delate, width=50 )
button3.place( x=275, y = 400)
button4 = Button(fenetre, text = "Rechecher un membre", command = alpha, width=50 )
button4.place( x=275, y = 450)
button5 = Button(fenetre, text = "Statistique",width=50, command = statistique)
button5.place( x=275, y = 500)
button6 = Button(fenetre, text="Quitter", command = destroy,width=50)
button6.place( x=275, y = 550)
