from tkinter import*
from tkinter.ttk import *
from pygame import*
import pygame
import tkinter as tk
import matplotlib.pyplot as plt

def supress(information1,information2):
     F = open("inscris.txt","r")
     maListe = []
     for l in F.readlines():
         ligne = l.split(",")
         maListe.append(ligne)
     for i in range(0,len(maListe)):
         ligne = maListe[i]
         if information1 == ligne[0]:
             if information2 == ligne[1]:
                 print(ligne)
                 maListe.remove(maListe[i]) ### on supprime la ligne que l'on veut supprimer dans notre liste
                 break
     F.close()
     F2 = open("inscris.txt","w")### on réecrit notre fichier avec notre nouvelle liste
     for i in range (0,len(maListe)):
          T = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(maListe[i][0],maListe[i][1],maListe[i][2],maListe[i][3],maListe[i][4],maListe[i][5],maListe[i][6],maListe[i][7],maListe[i][8],maListe[i][9],maListe[i][10],maListe[i][11])
          F2.write(T)
          print(T)
     F2.close()

def premierTraitement(value,premiereInformation): ### Cela permet de faire un premier trie dans notre fichier
     compteur = 0
     F = open ("inscris.txt", 'r')
     F2 = open ("recherche.txt", 'w')
     for l in F.readlines():
            liste1 = l.split(',')
            if value == "nom":
                if premiereInformation == liste1[0]:
                    F2.write(l) 
                    compteur = compteur + 1
            elif value == "prenom":
                if premiereInformation == liste1[1]:
                    F2.write(l) 
                    compteur = compteur + 1
            else:
                if premiereInformation == liste1[2]:
                    F2.write(l)
                    compteur = compteur + 1
     F2.close()
     F.close()
     return(compteur)

def modifListeComboBox(value): ### Cela permet de modifier les éléments que contient notre comboBox
     information = ["nom","prenom","tel"]
        
     if value == "nom":
            information.remove(information[0])
     elif value  == "prenom":
            information.remove(information[1])
     else:
            information.remove(information[2])
     FichierListe = open ("fichierListe.txt", 'w')
     T = "{0},{1}\n".format(information[0],information[1])
     FichierListe.write(T)
     FichierListe.close()
     
def infoMembre(a):
           def back():
                fenetre2.destroy()
           def modifier():
                A = str(entre1.get())
                B = str(entre2.get())
                Cbis = str(entre3.get())
                C = str(homme.get())
                D = str(femme.get())
                E = str(entre5.get())
                F = str(entre6.get())
                G = str(stk.get())
                H = str(katia.get())
                I = str(c.get())
                J = str(photoshop.get())
                K = str(latex.get())
                T = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}\n".format(A,B,Cbis,C,D,E,F,G,H,I,J,K)
                F = open("inscris.txt","r")
                maListe = []
                for l in F.readlines():
                   ligne = l.split(",")
                   maListe.append(ligne)
                for i in range(0,len(maListe)):
                   ligne = maListe[i]
                   if A == ligne[0]:
                        if B == ligne[1]:
                           maListe.remove(maListe[i]) ### on supprime la ligne que l'on veut supprimer dans notre liste
                           break
                F.close()
                F2 = open("inscris.txt","w")### on réecrit notre fichier avec notre nouvelle liste
                F2.write(T)
                for i in range (0,len(maListe)):
                    T2 = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(maListe[i][0],maListe[i][1],maListe[i][2],maListe[i][3],maListe[i][4],maListe[i][5],maListe[i][6],maListe[i][7],maListe[i][8],maListe[i][9],maListe[i][10],maListe[i][11])
                    F2.write(T2)
                F2.close()
                
           fenetre2 = Toplevel()
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
           Checkbutton2 = Checkbutton(fenetre2, text="Katia",variable = katia)
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

           button1 = Button(fenetre2, text="Retour", command = back)
           button1.grid(row = 10, column = 0)
           button2 = Button(fenetre2, text="Modifier", command = modifier)
           button2.grid(row = 10, column = 2)

           entre1.insert(0,a[0])
           entre2.insert(0,a[1])
           entre3.insert(0,a[2])
           entre5.insert(0,a[5])
           entre6.insert(0,a[6])
           
           if a[3] == str(1):
               homme.set(True)
           if a[4] == str(1):
               femme.set(True)
           if a[7] == str(1):
               stk.set(True)
           if a[8] == str(1):
               katia.set(True)
           if a[9] == str(1):
               c.set(True)
           if a[10] == str(1):
               photoshop.set(True)
           if a[11] == str(1):
               latex.set(True)

def true():

    def secondTraitement():
        value = C2.get()
        secondeInformation = str(e2.get())
        compteur2 = 0
        Fichier3 = open("recherche.txt","r")
        for l in Fichier3.readlines():
                liste1 = l.split(',')
                if value == "nom":
                    if secondeInformation == liste1[0]:
                        a = liste1
                        compteur2 = compteur2 + 1
                        break
                elif value == "prenom":
                    if secondeInformation == liste1[1]:
                        a = liste1
                        compteur2 = compteur2 + 1
                        break
                else:
                    if secondeInformation == liste1[2]:
                        a = liste1
                        compteur2 = compteur2 + 1
                        break
        Fichier3.close()
        if compteur2 == 1:
            infoMembre(a)
        else:
            ligne1 = "Nous n'avons aucune correspondance avec cette nouvelle information"
            label0.config(text="%s" %ligne1)
            compteur = 0


    FichierListe = open ("fichierListe.txt", 'r')
    a = FichierListe.readline()
    information=a.split(',')
    FichierListe.close()

        
    fenetre3 = Tk()
    
    fenetre3V1=PanedWindow(fenetre3)
    fenetre3V1.grid(row=0, column=0)
    fenetre3V2=PanedWindow(fenetre3)
    fenetre3V2.grid(row=1, column=0)
    
    l1 = Label(fenetre3V1, text = "Vueillez entrer une autre information sur la personne recherché")
    l1.grid(row = 0, column = 0)
    
    C2=Combobox (fenetre3V2,values=information)
    C2.grid(row=1,column=0)
    e2 = Entry(fenetre3V2)
    e2.grid(row = 1, column = 1)
    b2 = Button(fenetre3V2, text="Rechercher", command = secondTraitement)
    b2.grid(row = 1, column = 2)
    
    b3 = Button(fenetre3V2, text="Quitter", command = quit)
    b3.grid(row = 10, column = 0)

    label0 = Label(fenetre3V2, text = "...")
    label0.grid(row = 2, column = 1)
   
     
def false():
    fenetre3 = Tk()
    quote1 = """ """
    quote2 = """ """
    quote3 = """ """
    quote4 = """ """
    Fichier = open ("recherche.txt", 'r')
    for l in Fichier.readlines(): #le programme lit le fichier ligne par ligne
        a = l.split(',')#la ligne devient une liste
        b = a[0]
        c = a[1]
        d = a[2]
        quote1 = quote1 + b + "\n"#on ajoute la première valeur de la liste
        quote2 = quote2 + c + "\n"
        quote3 = quote3 + d + "\n"
    Fichier.close()

    text2 = Text(fenetre3, height=30, width=20)
    text2.insert(END, quote1, 'color')#on affiche la chaine de caractère dans la partie text2 de l'interface graphique
    text2.grid(row = 1, column = 1)

    text3 = Text(fenetre3, height=30, width=20)
    text3.insert(END, quote2, 'color')
    text3.grid(row = 1, column = 2)

    text4 = Text(fenetre3, height=30, width=20)
    text4.insert(END, quote3, 'color')
    text4.grid(row = 1, column = 3)

def interfaceSecondTraitement():
            fenetre2 = Tk()
            
            label0 = Label(fenetre2, text = "Avez vous une autre information sur la personne recherché?")
            label0.grid(row = 0, column = 1)
            
            button1 = Button(fenetre2, text="OUI", command = true)
            button1.grid(row = 1, column = 0)
            button2 = Button(fenetre2, text="NON",command = false)
            button2.grid(row = 1, column = 2)
            
def latex():
    pygame.init()
    son = pygame.mixer.Sound("music.wav")

    son.play()

    def back():
        son.stop()
        fenetre.destroy()


    fenetre = Toplevel()
    fenetre.geometry("780x500+400+120")
    fenetre.title("Ce n'est qu'un au revoir")

    img = PhotoImage(file="Capture.gif")
    canf1 = Canvas(fenetre, bg = 'blue', width = 780, height = 450)
    canf1.create_image(0,0,anchor = tk.NW, image = img)
    canf1.image = img
    canf1.grid(column = 0,row= 0)

    button1 = Button(fenetre, text = "Retour", command = back,width=30 )
    button1.grid(column = 0,row= 1)


def pasDeCorrespondance(premiereInformation):
     
           fenetre2 = Tk()

           label1 = Label(fenetre2, text = "...")
           label1.grid(row = 0, column = 1)
           label2 = Label(fenetre2, text = "...")
           label2.grid(row = 1, column = 1)

           texte1 = "nous n'avons aucune personne qui se nomme "
           texte2 = " dans notre répertoire"

           texte3 = "Vous avez peut être fait une faute d'orthographe en rentrant le nom"
           
           ligne1 = texte1+str(premiereInformation)+texte2
           label1.config(text="%s" %ligne1)
           label2.config(text="%s" %texte3)

           button1 = Button(fenetre2, text="Quitter", command = quit)
           button1.grid(row = 2, column = 0)
           button2 = Button(fenetre2, text="Retour")
           button2.grid(row = 2, column = 2)
    

def affichage(truc):
    quote1 = """ """
    quote2 = """ """
    quote3 = """ """
    quote4 = """ """
    quote5 = """ """
    quote6 = """ """
    quote7 = """ """

    Fichier = open ("inscris.txt", 'r')
    for l in Fichier.readlines(): #le programme lit le fichier ligne par ligne
        cours = str()
        sexe = str()
        r = l.split(',')#la ligne devient une liste
        nom = r[0]
        prenom = r[1]
        promo = r[2]
        if r[3] == str(1):
            sexe = str("homme")
        if r[4] == str(1):
            sexe = str("femme")
        mail= r[5]
        tel =  r[6]
        if r[7] == str(1):
            cours = cours + str("STK")
        if r[8] == str(1):
            cours = cours + str(",Catia")
        if r[9] == str(1):
           cours = cours + str(",C++")
        if r[10] == str(1):
            cours = cours + str(",Photoshop")
        if r[11] == str(1):
            cours = cours + str(",Latek")

            
        if truc == "normal":
             quote1 = quote1 + nom + "\n"#on ajoute la première valeur de la liste
             quote2 = quote2 + prenom + "\n"
             quote3 = quote3 + promo + "\n"
             quote4 = quote4 + sexe + "\n"
             quote5 = quote5 + mail + "\n"
             quote6 = quote6 + tel + "\n"
             quote7 = quote7 + cours + "\n"
        if truc == "STK":
             if r[7] == str(1):
                  quote1 = quote1 + nom + "\n"#on ajoute la première valeur de la liste
                  quote2 = quote2 + prenom + "\n"
                  quote3 = quote3 + promo + "\n"
                  quote4 = quote4 + sexe + "\n"
                  quote5 = quote5 + mail + "\n"
                  quote6 = quote6 + tel + "\n"
                  quote7 = quote7 + cours + "\n"
        if truc == "Katia":
             if r[8] == str(1):
                  quote1 = quote1 + nom + "\n"#on ajoute la première valeur de la liste
                  quote2 = quote2 + prenom + "\n"
                  quote3 = quote3 + promo + "\n"
                  quote4 = quote4 + sexe + "\n"
                  quote5 = quote5 + mail + "\n"
                  quote6 = quote6 + tel + "\n"
                  quote7 = quote7 + cours + "\n"
        if truc == "c":
             if r[9] == str(1):
                  quote1 = quote1 + nom + "\n"#on ajoute la première valeur de la liste
                  quote2 = quote2 + prenom + "\n"
                  quote3 = quote3 + promo + "\n"
                  quote4 = quote4 + sexe + "\n"
                  quote5 = quote5 + mail + "\n"
                  quote6 = quote6 + tel + "\n"
                  quote7 = quote7 + cours + "\n"
        if truc == "Photochop":
             if r[10] == str(1):
                  quote1 = quote1 + nom + "\n"#on ajoute la première valeur de la liste
                  quote2 = quote2 + prenom + "\n"
                  quote3 = quote3 + promo + "\n"
                  quote4 = quote4 + sexe + "\n"
                  quote5 = quote5 + mail + "\n"
                  quote6 = quote6 + tel + "\n"
                  quote7 = quote7 + cours + "\n"
        if truc == "Latex":
             if r[11] == str(1):
                  quote1 = quote1 + nom + "\n"#on ajoute la première valeur de la liste
                  quote2 = quote2 + prenom + "\n"
                  quote3 = quote3 + promo + "\n"
                  quote4 = quote4 + sexe + "\n"
                  quote5 = quote5 + mail + "\n"
                  quote6 = quote6 + tel + "\n"
                  quote7 = quote7 + cours + "\n"
                  
    Fichier.close()
    return(quote1,quote2,quote3,quote4,quote5,quote6,quote7)

def modiferV2():
     recupDeValeur = []
     F = open('fichierListe.txt','r')
     for i in F.readlines():
          recupDeValeur.append(i)
     F.close()
     T = recupDeValeur[0]
     nomDuFichier = recupDeValeur[1]
     
     liste1 = T.split(',')
     maListe =[]
     F = open(nomDuFichier,'r')
     for l in F.readlines():
           ligne = l.split(",")
           maListe.append(ligne)
     for i in range(0,len(maListe)):
          ligne = maListe[i]
          if liste1[0] == ligne[0]:
               if liste1[1] == ligne[1]:
                    maListe.remove(maListe[i]) ### on supprime la ligne que l'on veut supprimer dans notre liste
                    break
     F.close()
     
     F2 = open(nomDuFichier,"w")### on réecrit notre fichier avec notre nouvelle liste
     F2.write(T)
     for i in range (0,len(maListe)):
          T2 = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(maListe[i][0],maListe[i][1],maListe[i][2],maListe[i][3],maListe[i][4],maListe[i][5],maListe[i][6],maListe[i][7],maListe[i][8],maListe[i][9],maListe[i][10],maListe[i][11])
          F2.write(T2)
     F2.close()

def modifNom():
     liste = []
     F = open('fichierListe.txt','r')
     L = F.readline()
     F.close()
     recupDeValeur = L.split(',')
     print(recupDeValeur)
     
     def modiferV3():
          newName = entre666.get()
          fenetreJeNeSaisPlusCombien.destroy()
          recupDeValeur[1] = newName
          T2 ="{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}".format(recupDeValeur[0],recupDeValeur[1],recupDeValeur[2],recupDeValeur[3],recupDeValeur[4],recupDeValeur[5],recupDeValeur[6],recupDeValeur[7],recupDeValeur[8],recupDeValeur[9],recupDeValeur[10],recupDeValeur[11])
          F = open('inscris.txt','a')
          F.write(T2)
          F.close()
          
     fenetreJeNeSaisPlusCombien = Tk()
     fenetreJeNeSaisPlusCombien.geometry("550x250+500+200")
     label0 = Label(fenetreJeNeSaisPlusCombien, text = "Pouvez vous modifer le prénom")
     label0.grid(row = 0, column = 1)

     entre666 = Entry(fenetreJeNeSaisPlusCombien)
     entre666.grid(row = 1, column = 1)

     entre666.insert(0,recupDeValeur[1])

     button1 = Button(fenetreJeNeSaisPlusCombien, text="Enregistrer",command = modiferV3)
     button1.grid(row = 2, column = 1)
               
def choix():
     def retour():
          fenetre2.destroy()

     recupDeValeur = []
     F = open('fichierListe.txt','r')
     for i in F.readlines():
          recupDeValeur.append(i)
     F.close()

     L = recupDeValeur[0]
     r = L.split(',')
                         
     fenetre2 = Tk()
     fenetre2.geometry("550x250+500+200")

     texte = "il y a déjà une personne qui se nomme "+r[0]," ",r[1]

     label0 = Label(fenetre2, text = texte)
     label0.grid(row = 0, column = 1)

     button1 = Button(fenetre2, text="Modifier la base de donnée",command = modiferV2)
     button1.grid(row = 1, column = 1)
     button2 = Button(fenetre2, text="Modifier le prénom que vous voulez entrer", command = modifNom)
     button2.grid(row = 2, column = 1)

     buttonRetour = Button(fenetre2, text="Retour",command = retour)
     buttonRetour.grid(row = 3, column = 0)

def graph():
        nombreHomme = 0
        nombreFemme = 0
        nombreSTK = 0
        nombreCatia = 0
        nombreC = 0
        nombrePhotoshop = 0
        nombrelatek = 0
        nombreAero1 = 0
        nombreAero2 = 0
        nombreAero3 = 0
        nombreAero4 = 0
        nombreAero5 = 0


        Fichier = open ("inscris.txt", 'r')
        for l in Fichier.readlines():
            liste = l.split(',')
            if liste[3] == str(1):
                nombreHomme = nombreHomme +1
            if liste[4] == str(1):
                nombreFemme = nombreFemme +1
            if liste[7] == str(1):
                nombreSTK = nombreSTK + 1
            if liste[8] == str(1):
                nombreCatia = nombreCatia + 1 
            if liste[9] == str(1):
                nombreC = nombreC + 1
            if liste[10] == str(1):
                nombrePhotoshop = nombrePhotoshop + 1
            if liste[11] == str(1):
                nombrelatek = nombrelatek + 1
            if liste[2] == "aéro1":
                nombreAero1 = nombreAero1 + 1
            if liste[2] == "aéro2":
                nombreAero2 = nombreAero2 + 1
            if liste[2] == "aéro3":
                nombreAero3 = nombreAero3 + 1
            if liste[2] == "aéro4":
                nombreAero4 = nombreAero4 + 1
            if liste[2] == "aéro5":
                nombreAero5 = nombreAero5 + 1
        Fichier.close()

        name = ['Homme', 'Femme']
        data = [nombreHomme,nombreFemme]
        explode=(0, 0)
        plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
        plt.axis('equal')
        plt.savefig('stat1.png')
        plt.close()
        plt.show()
        

        name = ['STK', 'CATIA','C++','Photoshop','latek']
        data = [nombreSTK,nombreCatia,nombrePhotoshop,nombreC, nombrelatek]
        explode=(0,0,0,0,0)
        plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
        plt.axis('equal')
        plt.savefig('stat2.png')
        plt.close()
        plt.show()

        name = ['Aéro1', 'Aéro2','Aéro3','Aéro4','Aéro5']
        data = [nombreAero1,nombreAero2,nombreAero3,nombreAero4, nombreAero5]
        explode=(0,0,0,0,0)
        plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
        plt.axis('equal')
        plt.savefig('stat3.png')
        plt.close()
        plt.show()
     
     
