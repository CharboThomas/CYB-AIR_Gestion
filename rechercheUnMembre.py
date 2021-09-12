from tkinter import*
from tkinter.ttk import *
from maBibiliotheque import*

information = ["nom","prenom","tel"]

def alpha():
    def retour():
        fenetre.destroy()
    def rechercherUnPersonne():  
        value = C1.get()
        premiereInformation = str(e1.get())
        
        compteur = premierTraitement(value,premiereInformation)

        modifListeComboBox(value)
        
        if compteur > 1:
            fenetre.destroy
            interfaceSecondTraitement()
            
        elif compteur == 1 :
            fenetre.destroy()
            Fichier2 = open("recherche.txt",'r')### j'ouvre le fichier dans lequel j'ai enregistrer toutes les correspondances
            information = Fichier2.readline()
            a = information.split(',')
            Fichier2.close()
            infoMembre(a)
            
        else:
           fenetre.destroy()
           pasDeCorrespondance(premiereInformation)
              
           
    fenetre = Tk()
    fenetre.geometry("400x250+500+200")
    fenetre.title("Recherche")

    l1 = Label(fenetre, text = "trouver un membre")
    l1.grid(row = 0, column = 1)

    C1=Combobox (fenetre,values=information)
    C1.grid(row=1,column=0)
    e1 = Entry(fenetre)
    e1.grid(row = 1, column = 1)
    b2 = Button(fenetre, text="Rechercher",command = rechercherUnPersonne)
    b2.grid(row = 1, column = 2)
     
     
    button1 = Button(fenetre, text="Retour", command = retour)
    button1.grid(row = 2, column = 0)

