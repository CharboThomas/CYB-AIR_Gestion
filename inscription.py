from tkinter import*
import tkinter as tk
from maBibiliotheque import*

T = "0"
G = 1
      
def register():
    def retour():
        fenetre2.destroy()
    def registeur():
        
         etat = 0
         compteurLigne = 0
         
         A = str(entre1.get())
         B = str(entre2.get())
         Cbis = str(entre3.get())
         C = str(homme.get())
         D = str(femme.get())
         E = str(entre5.get())
         F = str(entre6.get())
         
         G = str(stk.get())
         print(G)
         H = str(katia.get())
         I = str(c.get())
         J = str(photoshop.get())
         K = str(latex.get())
         
         entre1.delete(0,END)
         entre2.delete(0,END)
         entre3.delete(0,END)
         entre5.delete(0,END)
         entre6.delete(0,END)
         
         T = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}\n".format(A,B,Cbis,C,D,E,F,G,H,I,J,K)
         
         FichierControle = open ("inscris.txt", 'r')
         
         for l in FichierControle.readlines():
             r = l.split(',')
             compteurLigne = compteurLigne+1
             if A == r[0]:
                 if B == r[1]:
                     nomDuFichier = "inscris.txt"
                     
                     F = open('fichierListe.txt','w')
                     F.write(T)
                     F.write(nomDuFichier)
                     F.close()

                     choix() 
                     
                     etat = 1 
                     
         FichierControle.close()

         if etat == 0: ### enregistrer le nouveau membre
             FichierEnregistrement = open ("inscris.txt", 'a')       
             FichierEnregistrement.write(T)
             FichierEnregistrement.tell() 
             FichierEnregistrement.close()
             
         fenetre2.destroy()
        
    fenetre2 = Toplevel()
    fenetre2.geometry("280x300+500+200")
    fenetre2.title("Fiche d'inscription")


    label0 = Label(fenetre2, text = "Fiche d'incription")
    label0.grid(row = 0, column = 1)

    label1 = Label(fenetre2, text = "Nom:")
    label1.grid(row = 1, column = 0)
    label2 = Label(fenetre2, text = "Prénom:")
    label2.grid(row = 2, column = 0)
    label3 = Label(fenetre2, text = "Année:")
    label3.grid(row = 3, column = 0)
    label4 = Label(fenetre2, text = "Sexe:")
    label4.grid(row = 4, column = 0)
    label5 = Label(fenetre2, text = "E mail:")
    label5.grid(row = 5, column = 0)
    label6 = Label(fenetre2, text = "Téléphone:")
    label6.grid(row = 6, column = 0)
    label7 = Label(fenetre2, text = "Cours suivi:")
    label7.grid(row = 7, column = 0)

    entre1 = Entry(fenetre2)
    entre1.grid(row = 1, column = 1)
    entre2 = Entry(fenetre2)
    entre2.grid(row = 2, column = 1)
    entre3 = Entry(fenetre2)
    entre3.grid(row = 3, column = 1)
    entre5 = Entry(fenetre2)
    entre5.grid(row = 5, column = 1)
    entre6 = Entry(fenetre2)
    entre6.grid(row = 6, column = 1)
    
    stk = IntVar()
    Checkbutton1 = Checkbutton(fenetre2, text="STK",variable = stk)
    Checkbutton1.grid(row = 8, column = 0)
    katia = IntVar()
    Checkbutton2 = Checkbutton(fenetre2, text="Catia",variable = katia)
    Checkbutton2.grid(row = 8, column = 1)
    c = IntVar()
    Checkbutton3 = Checkbutton(fenetre2, text="C++",variable = c)
    Checkbutton3.grid(row = 8, column = 2)
    photoshop = IntVar()
    Checkbutton4 = Checkbutton(fenetre2, text="Photoshop",variable = photoshop)
    Checkbutton4.grid(row = 9, column = 1)
    latex = IntVar()
    Checkbutton5 = Checkbutton(fenetre2, text="Latex",variable = latex)
    Checkbutton5.grid(row = 9, column = 2)

    homme = IntVar()
    Checkbutton6 = Checkbutton(fenetre2, text="Homme",variable = homme)
    Checkbutton6.grid(row = 4, column = 1)
    femme = IntVar()
    Checkbutton7 = Checkbutton(fenetre2, text="Femme",variable = femme)
    Checkbutton7.grid(row = 4, column = 2)

    button1 = Button(fenetre2, text="Retour", command = retour)
    button1.grid(row = 10, column = 0)
    button2 = Button(fenetre2, text="Enregistrer",command = registeur)
    button2.grid(row = 10, column = 2)

